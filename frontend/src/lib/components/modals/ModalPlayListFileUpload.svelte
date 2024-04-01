<script>
	import { closeModal } from 'svelte-modals';
	import UploadFile from '../playlist/UploadFile.svelte';
	import { onMount } from 'svelte';

	// provided by <Modals />
	export let isOpen;

	export let playlist;
	export let onUpdated;
	export let asset;
	export let open_file_browser;
	function asset_added(event) {
		let playlist = event.detail;
		onUpdated(playlist);
		closeModal();
	}
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<!-- exit button -->
			<button class="btn exit-btn" on:click={closeModal}>X</button>

			<UploadFile {playlist} on:added={asset_added} {asset} {open_file_browser} />
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
