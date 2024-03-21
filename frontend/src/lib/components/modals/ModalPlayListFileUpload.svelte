<script>
	import { closeModal } from 'svelte-modals';
	import UploadFile from '../playlist/UploadFile.svelte';

	// provided by <Modals />
	export let isOpen;

	export let playlist;
	export let onAdded;
	function asset_added(event) {
		console.log('asset_added', event.detail);
		let asset = event.detail;
		onAdded(asset);
		closeModal();
	}
</script>

{#if isOpen}
	<div role="dialog" class="modal">
		<div class="contents">
			<UploadFile {playlist} on:added={asset_added} />
		</div>
	</div>
{/if}

<style>
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
