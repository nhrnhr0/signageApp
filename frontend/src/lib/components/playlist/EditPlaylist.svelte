<script>
	import AssetsManager from './AssetsManager.svelte';
	import PlaylistService from '$lib/services/playlists';
	import { createEventDispatcher } from 'svelte';
	export const dispatch = createEventDispatcher();
	export let playlist;
	let submiting = false;
	function submit() {
		submiting = true;
		PlaylistService.updateOrCreatePlaylist(playlist)
			.then((resp) => {
				console.log(resp);
				dispatch('save', playlist);
			})
			.catch((e) => {
				console.log(e);
			})
			.finally(() => {
				submiting = false;
			});
	}
</script>

<div class="container mt-5">
	<h2>
		{#if playlist.uuid}
			עריכת פלייליסט: {playlist.name}
		{:else}
			יצירת פלייליסט
		{/if}
	</h2>
	<form action="" method="post" enctype="multipart/form-data">
		<!-- is_active -->
		<div class="form-group form-check">
			<input
				type="checkbox"
				class="form-check-input"
				id="is_active"
				name="is_active"
				bind:checked={playlist.is_active}
			/>
			<label class="form-check-label" for="is_active">פעיל</label>
		</div>
		<!-- name -->
		<div class="form-group">
			<label for="name">שם</label>
			<input type="text" class="form-control" id="name" name="name" bind:value={playlist.name} />
		</div>
		<!-- islands selection -->

		<button
			type="submit"
			class="btn btn-primary"
			on:click|preventDefault={submit}
			disabled={submiting}>שמור</button
		>
		<AssetsManager bind:playlist />
	</form>
</div>
