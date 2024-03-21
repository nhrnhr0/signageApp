<script>
	import { createEventDispatcher, onMount } from 'svelte';
	import PlaylistsService from '$lib/services/playlists';
	const dispatch = createEventDispatcher();

	export let playlist;

	let file_name = null;
	let duration = null;
	let type = null;
	let _file = null;

	function submit() {
		if (!_file) {
			return;
		}
		if (playlist.uuid) {
			upload();
		} else {
			PlaylistsService.createPlaylist(playlist).then((data) => {
				playlist = data;
				upload();
			});
		}
	}
	function upload() {
		PlaylistsService.uploadAsset(playlist.uuid, _file, duration, type).then((res) => {
			// add the asset to the playlist
			playlist.assets.push(res);
			dispatch('added', playlist);
		});
	}

	function file_changed(e) {
		const file = e.target.files[0];
		_file = file;
		const file_extension = file.name.split('.').pop();
		const _type = file_extension === 'mp4' ? 'video' : 'image';
		type = _type;
		let display = document.getElementById('file-display');
		if (type === 'video') {
			// get the duration of the video
			// const video = document.createElement('video');
			// video.src = URL.createObjectURL(file);
			// video.onloadedmetadata = function () {
			// 	duration = video.duration;
			// };
			duration = -1;
			display.innerHTML = `<video controls autoplay loop muted width="200">
                <source src=${URL.createObjectURL(file)} type="video/mp4" />
                Your browser does not support the video tag.
            </video>`;
		} else {
			if (duration === null) {
				duration = 10;
			}
			display.innerHTML = `<img src=${URL.createObjectURL(file)} width="200"
            alt="file" />`;
		}
	}
	onMount(() => {
		let el = document.querySelector('input[type="file"]#file');
		el.focus();
		el.click();
	});
</script>

<form action="" method="post" enctype="multipart/form-data" on:submit|preventDefault={submit}>
	<!-- file -->
	<div class="form-group">
		<label for="file">קובץ</label>
		<input
			type="file"
			id="file"
			name="file"
			class="form-control"
			on:change={file_changed}
			bind:value={file_name}
			accept="image/*,video/*"
		/>
		<div id="file-display">
			<!-- {#if file}
				{#if type === 'image'}
					<img src={URL.createObjectURL(file)} alt="file" />
				{:else if type === 'video'}
					<video controls autoplay loop muted>
						<source src={URL.createObjectURL(file)} type="video/mp4" />
						Your browser does not support the video tag.
					</video>
				{/if}
			{/if} -->
		</div>
	</div>
	<!-- duration -->
	<div class="form-group">
		<label for="duration">משך</label>
		<input
			type="number"
			id="duration"
			name="duration"
			class="form-control"
			bind:value={duration}
			step="0.01"
		/>
	</div>

	<!-- type -->
	<div class="form-group">
		<label for="type">סוג</label>
		<select id="type" name="type" class="form-control" bind:value={type}>
			<option value="image">תמונה</option>
			<option value="video">וידאו</option>
		</select>
	</div>

	<button type="submit" class="btn btn-primary">העלה</button>
</form>
