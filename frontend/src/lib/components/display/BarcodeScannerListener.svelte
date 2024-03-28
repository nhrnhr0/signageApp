<script>
	import { browser } from '$app/environment';
	import { onDestroy, onMount } from 'svelte';

	// listen to keypress event on the document to find out if a barcode scanner is used
	// if a barcode scanner is used, the keypress event will be fired multiple times in a short period of time
	// at the end of the burst of keypress events, this component will call scaned(chars) with the scanned barcode
	let _barcode = '';
	/**
	 * @type {(barcode: string) => void}
	 */
	export let onScaned;
	/**
	 * @type {number}
	 */
	let timeout;
	onMount(() => {
		if (!browser) return;
		window.document.addEventListener('keypress', listenr);
	});

	/**
	 *
	 * @param event {KeyboardEvent}
	 */
	function listenr(event) {
		_barcode += event.key;
		timeout && clearTimeout(timeout);
		timeout = setTimeout(() => {
			if (_barcode.length > 1) {
				if (onScaned) onScaned(_barcode);
			}
			_barcode = '';
		}, 500);
	}
	onDestroy(() => {
		if (!browser) return;
		if (listenr) {
			window.document.removeEventListener('keypress', listenr);
		}
	});
</script>
