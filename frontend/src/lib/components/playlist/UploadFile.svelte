<script>
	import { createEventDispatcher, onMount } from 'svelte';
	import PlaylistsService from '$lib/services/playlists';
	import { BACKEND_MEDIA_URL } from '$lib/consts';
	const dispatch = createEventDispatcher();

	export let playlist;
	export let asset = null;
	let file_name = asset ? asset.name : null;
	let duration = asset ? asset.duration : null;
	let type = asset ? asset.type : 'image';
	let _file = asset ? BACKEND_MEDIA_URL + asset.media : null;

	export let open_file_browser = false;

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
		PlaylistsService.uploadAsset(playlist.uuid, asset?.id, _file, duration, type).then((res) => {
			// add the asset to the playlist
			if (!asset?.id) {
				playlist.assets.push(res);
			} else {
				// update the asset
				let index = playlist.assets.findIndex((a) => a.id === asset.id);
				playlist.assets[index] = res;
			}
			dispatch('added', playlist);
		});
	}

	function delete_asset(asset) {
		PlaylistsService.deleteAsset(playlist.uuid, asset.id).then((res) => {
			let index = playlist.assets.findIndex((a) => a.id === asset.id);
			playlist.assets.splice(index, 1);
			dispatch('deleted', playlist);
		});
	}

	function file_changed(e) {
		const file = e.target.files[0];
		_file = file;
		const file_extension = file.name.split('.').pop();
		const _type = file_extension === 'mp4' ? 'video' : 'image';
		type = _type;
		set_file_preview(URL.createObjectURL(file), type);
	}

	// function set_file_preview(file) {
	// 	const file_extension = file.name.split('.').pop();
	// 	const _type = file_extension === 'mp4' ? 'video' : 'image';
	// 	type = _type;
	// 	let display = document.getElementById('file-display');
	// 	if (type === 'video') {
	// 		// get the duration of the video
	// 		// const video = document.createElement('video');
	// 		// video.src = URL.createObjectURL(file);
	// 		// video.onloadedmetadata = function () {
	// 		// 	duration = video.duration;
	// 		// };
	// 		duration = -1;
	// 		display.innerHTML = `<video controls autoplay loop muted width="200">
	//             <source src=${URL.createObjectURL(file)} type="video/mp4" />
	//             Your browser does not support the video tag.
	//         </video>`;
	// 	} else {
	// 		if (duration === null) {
	// 			duration = 10;
	// 		}
	// 		display.innerHTML = `<img src=${URL.createObjectURL(file)} width="200"
	//         alt="file" />`;
	// 	}
	// }

	function set_file_preview(file_url, type) {
		let display = document.getElementById('file-display');
		if (!display) return;
		if (type === 'video') {
			duration = -1;
			display.innerHTML = `video controls autoplay loop muted width="200">
                <source src=${file_url} type="video/mp4" />
                Your browser does not support the video tag.
            </video>`;
		}
		if (type === 'image') {
			if (duration === null) {
				duration = 10;
			}
			display.innerHTML = `<img src=${file_url} width="200"
			alt="file" />`;
		}
	}
	onMount(() => {
		if (open_file_browser) {
			let el = document.querySelector('input[type="file"]#file');
			if (!el) return;
			el.focus();
			el.click();
		}
		if (asset) {
			let _file = BACKEND_MEDIA_URL + asset.media;
			set_file_preview(_file, asset.type);
		}
	});
</script>

<form action="" method="post" enctype="multipart/form-data" on:submit|preventDefault={submit}>
	<!-- file -->
	<div class="form-group">
		<label for="file">קובץ</label>
		<!-- {JSON.stringify(asset)} -->
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
	<div class="d-flex" style="justify-content: space-between;">
		<button type="submit" class="btn btn-primary">
			{#if asset}עדכן{:else}הוסף{/if}
		</button>

		{#if asset}
			<button type="button" class="btn btn-danger" on:click={delete_asset(asset)}> מחק </button>
		{/if}
	</div>
</form>
