<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import ScreenService from '$lib/services/screens';
	import DisplayMainWith4Subs from '$lib/components/display/DisplayMainWith4Subs.svelte';
	import DisplayFullScreen from '$lib/components/display/DisplayFullScreen.svelte';

	const code = $page.params.code;
	let data = null;
	onMount(async () => {
		ScreenService.getScrenDisplayByCode(code).then((_data) => {
			data = _data;
		});
	});
</script>

{#if data === null}
	<div>{code}</div>
{:else if data.layout == 'MainWith4Subs'}
	<DisplayMainWith4Subs {data} />
{:else if data.layout == 'FullScreen'}
	<DisplayFullScreen {data} />
{:else}
	<div>Unknown layout</div>
{/if}
