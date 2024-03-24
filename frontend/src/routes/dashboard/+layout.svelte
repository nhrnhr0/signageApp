<script>
	import Navbar from '$lib/components/shared/navbar.svelte';
	import { Modals, closeModal } from 'svelte-modals';

	function promptCloseModal() {
		// let result = confirm('Are you sure you want to close this modal?');
		// if (result) {
		// 	closeModal();
		// }
	}
</script>

<Navbar />
<Modals>
	<div slot="backdrop" class="backdrop" on:click={promptCloseModal} />
</Modals>
<slot />

<style>
	.backdrop {
		position: fixed;
		top: 0;
		bottom: 0;
		right: 0;
		left: 0;
		background: rgba(0, 0, 0, 0.5);
		z-index: 1;
	}
</style>
