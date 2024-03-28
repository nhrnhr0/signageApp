<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import ScreenService from '$lib/services/screens';
	import DisplayMainWith4Subs from '$lib/components/display/DisplayMainWith4Subs.svelte';
	import DisplayFullScreen from '$lib/components/display/DisplayFullScreen.svelte';
	import { browser } from '$app/environment';
	import BarcodeScannerListener from '$lib/components/display/BarcodeScannerListener.svelte';
	import authService from '$lib/auth';

	const code = $page.params.code;
	authService.protected_route();
	let data = null;
	onMount(async () => {
		ScreenService.getScrenDisplayByCode(code).then((_data) => {
			data = _data;
		});
	});
</script>

<BarcodeScannerListener
	onScaned={(bar) => {
		console.log(bar);

		alert(bar);
	}}
/>
{#if data === null}
	<div>{code}</div>
{:else if data.layout == 'MainWith4Subs'}
	<DisplayMainWith4Subs {data} />
{:else if data.layout == 'FullScreen'}
	<DisplayFullScreen {data} />
{:else}
	<div>Unknown layout</div>
{/if}
