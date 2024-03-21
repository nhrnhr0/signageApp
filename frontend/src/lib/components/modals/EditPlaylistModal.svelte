<script>
	import { closeModal } from 'svelte-modals';
	import EditPlaylist from '../playlist/EditPlaylist.svelte';
	import { onMount } from 'svelte';
	import PlaylistSerice from '$lib/services/playlists';

	// provided by <Modals />
	export let isOpen;

	export let playlist_uuid;
	export let onUpdated;
	let playlist;
	function asset_added(event) {
		console.log('asset_added', event.detail);
		let playlist = event.detail;
		onUpdated(playlist);
		closeModal();
	}
	onMount(() => {
		console.log('EditPlaylistModal onMount');
		PlaylistSerice.getPlaylist(playlist_uuid).then((data) => {
			console.log('EditPlaylistModal onMount getPlaylist', data);
			playlist = data;
		});
	});
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<!-- exit button -->
			<button class="btn exit-btn" on:click={closeModal}>X</button>
			{#if playlist}
				<EditPlaylist {playlist} />
			{/if}
		</div>
	</div>
{/if}

<style>
	.exit-btn {
		position: absolute;
		top: 0;
		left: 0;
	}
	.exit-btn:hover {
		background-color: red;
		color: white;
	}
	.modal {
		position: fixed;
		top: 0;
		bottom: 0;
		right: 0;
		left: 0;
		display: flex;
		justify-content: center;
		align-items: center;

		/* allow click-through to backdrop */
		pointer-events: none;
	}

	.contents {
		min-width: 240px;
		border-radius: 6px;
		padding: 16px;
		background: white;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		pointer-events: auto;
		position: relative;
	}

	h2 {
		text-align: center;
		font-size: 24px;
	}

	p {
		text-align: center;
		margin-top: 16px;
	}

	.actions {
		margin-top: 32px;
		display: flex;
		justify-content: flex-end;
	}
</style>
