<script>
	import { page } from '$app/stores';
	import AuthService from '$lib/auth';
	import Spinner from '$lib/components/shared/Spinner.svelte';
	import PlaylistsService from '$lib/services/playlists';
	import { onMount } from 'svelte';
	import EditPlaylist from '$lib/components/playlist/EditPlaylist.svelte';
	import { goto } from '$app/navigation';
	AuthService.protected_route();
	const uuid = $page.params.uuid;
	let playlist = null;
	onMount(async () => {
		playlist = await PlaylistsService.getPlaylist(uuid);
	});
</script>

{#if playlist === null}
	<Spinner />
{:else}
	<EditPlaylist
		bind:playlist
		on:save={(pl) => {
			goto(`/dashboard/playlists/`);
		}}
	/>
{/if}
