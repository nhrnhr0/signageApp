<script>
	import DashboardFullScreen from './display/DashboardFullScreen.svelte';
	import DashboardMainWith4Subs from './display/DashboardMainWith4Subs.svelte';

	export let screen;
</script>

<!-- based on the layout (FullScreen/MainWith4Subs), display it and inside each island show it's playlist's names -->
{#if screen.layout === 'FullScreen'}
	<DashboardFullScreen {screen} />
{:else if screen.layout === 'MainWith4Subs'}
	<DashboardMainWith4Subs bind:screen />
{/if}
