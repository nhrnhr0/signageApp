<script>
	import AuthService from '$lib/auth';
	import ScreensService from '$lib/services/screens';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	AuthService.protected_route();
	let screens = [];
	onMount(async () => {
		try {
			let resp = await ScreensService.getScreens();
			screens = resp;
		} catch (e) {
			screens = [];
		}
	});
</script>

<h2>מסכים</h2>
<ul>
	{#each screens as screen}
		<li>
			<div>
				<a href="/dashboard/screens/detail/?id={screen.uuid}">{screen.name}</a>
			</div>
		</li>
	{/each}
</ul>
