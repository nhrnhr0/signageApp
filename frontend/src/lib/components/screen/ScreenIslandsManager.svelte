<script>
	import DisplayFullScreen from './display/DisplayFullScreen.svelte';
	import DisplayMainWith4Subs from './display/DisplayMainWith4Subs.svelte';

	export let screen;
</script>

<!-- based on the layout (FullScreen/MainWith4Subs), display it and inside each island show it's playlist's names -->
{#if screen.layout === 'FullScreen'}
	<DisplayFullScreen {screen} />
{:else if screen.layout === 'MainWith4Subs'}
	<DisplayMainWith4Subs {screen} />
{/if}
