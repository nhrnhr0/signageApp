<script>
	import { page } from '$app/stores';
	import { onDestroy, onMount } from 'svelte';
	import ScreenService from '$lib/services/screens';
	import DisplayMainWith4Subs from '$lib/components/display/DisplayMainWith4Subs.svelte';
	import DisplayFullScreen from '$lib/components/display/DisplayFullScreen.svelte';
	import { browser } from '$app/environment';
	import BarcodeScannerListener from '$lib/components/display/BarcodeScannerListener.svelte';
	import authService from '$lib/auth';

	let code = undefined; // $page.params.code;

	let data = null;
	let interval = null;
	onMount(() => {
		authService.protected_route();

		code = $page.url.searchParams.get('id');
		ScreenService.getScrenDisplayByCode(code).then((_data) => {
			data = _data;
		});

		// set date fetching interval
		interval = setInterval(
			() => {
				ScreenService.getScrenDisplayByCode(code)
					.then((_data) => {
						console.log('fetched screen display: ', code, ' ', _data);
						data = _data;
					})
					.catch((error) => {
						console.error('Failed to fetch screen display:', error);
					});
			},
			1000 * 60 * 2
		); // 2 minute
	});

	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<BarcodeScannerListener
	onScaned={(bar) => {
		alert(bar);
	}}
/>
{#if data === null}
	<div>{code}</div>
{:else if data.is_active}
	{#if data.layout == 'MainWith4Subs'}
		<DisplayMainWith4Subs {data} />
	{:else if data.layout == 'FullScreen'}
		<DisplayFullScreen {data} />
	{:else}
		<div>תצוגה לא נתמכת</div>
	{/if}
{:else}
	<div>מסך לא פעיל</div>
{/if}
