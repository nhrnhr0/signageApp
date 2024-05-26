<script>
	import { page } from '$app/stores';
	import AuthService from '$lib/auth';
	import Spinner from '$lib/components/shared/Spinner.svelte';
	import PlaylistsService from '$lib/services/playlists';
	import { onMount } from 'svelte';
	import EditPlaylist from '$lib/components/playlist/EditPlaylist.svelte';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';

	AuthService.protected_route();
	let uuid = undefined;
	let playlist = null;
	onMount(async () => {
		uuid = $page.url.searchParams.get('id');
		debugger;
		console.log('uuid: ', uuid);
		playlist = await PlaylistsService.getPlaylist(uuid);
	});
</script>

{#if playlist === null || !uuid}
	<Spinner />
{:else}
	<EditPlaylist
		bind:playlist
		on:save={(pl) => {
			goto(`/dashboard/playlists/`);
		}}
	/>
{/if}
