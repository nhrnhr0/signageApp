<script>
	import AuthService from '$lib/auth';
	import PlaylistsService from '$lib/services/playlists';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
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

<h1 class="mb-4 mt-4">פלייליסטים</h1>
<!-- create new playlist button -->
<a href="/dashboard/playlists/new" class="btn btn-primary">צור פלייליסט חדש</a>
<h2 class="mb-4 mt-4">רשימת פלייליסטים</h2>
<ul>
	{#each playlists as playlist}
		<li>
			<div>
				<a href="{$page.url}/{playlist.uuid}">{playlist.name}</a>
			</div>
		</li>
	{/each}
</ul>
