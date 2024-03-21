<script>
	import AuthService from '$lib/auth';
	import PlaylistsService from '$lib/network.js';
	import { onMount } from 'svelte';
	AuthService.protected_route();
	let playlists = [];
	onMount(async () => {
		playlists = await PlaylistsService.getPlaylists();
	});
</script>

<h2>פלייליסטים</h2>
<ul>
	{#each playlists as playlist}
		<li>
			<div>
				<a href="/playlists/{playlist.uuid}">{playlist.name}</a>
			</div>
		</li>
	{/each}
</ul>
