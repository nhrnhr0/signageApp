<script>
	import AuthService from '$lib/auth';
	import PlaylistsService from '$lib/network.js';
	import { onMount } from 'svelte';
	AuthService.protected_route();
	let playlists = [];
	onMount(async () => {
		try {
			let resp = await PlaylistsService.getPlaylists();
			playlists = resp;
		} catch (e) {
			console.log(e);
			playlists = [];
		}
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
