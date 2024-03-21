<script>
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import AuthService, { isLoggedIn } from '$lib/auth';
	import AssetsManager from '$lib/components/playlist/AssetsManager.svelte';
	import IslandsManager from '$lib/components/playlist/IslandsManager.svelte';
	import Spinner from '$lib/components/shared/Spinner.svelte';
	import PlaylistsService from '$lib/network.js';
	import { onMount } from 'svelte';
	AuthService.protected_route();
	const uuid = $page.params.uuid;
	let playlist = null;
	onMount(async () => {
		playlist = await PlaylistsService.getPlaylist(uuid);
	});
</script>

<!--
{
    "uuid": "37d937b4-455c-4c07-ad5f-310c3c25d0e8",
    "name": "גנרי לכולם",
    "is_active": true,
    "start_at": null,
    "end_at": null,
    "assets": [
        {
            "id": 1,
            "name": "לוגו 1",
            "media": "/assets/favicon.png",
            "type": "image",
            "duration": 10
        }
    ],
    "island": [
        {
            "id": 1,
            "name": "main",
            "screens": [
                {
                    "uuid": "6a536d4a-38b3-461b-a1b8-3b425e59aa83",
                    "name": "מסך 1",
                    "is_active": true,
                    "layout": "MainWith4Subs"
                }
            ]
        }
    ]
}
-->
{#if playlist === null}
	<Spinner />
{:else}
	<div class="container mt-5">
		<h2>פלייליסט: {playlist?.name}</h2>
		<form action="" method="post" enctype="multipart/form-data">
			<!-- is_active -->
			<div class="form-group form-check" style="z-index: -1;">
				<input
					type="checkbox"
					class="form-check-input"
					id="is_active"
					name="is_active"
					checked={playlist.is_active}
				/>
				<label class="form-check-label" for="is_active">פעיל</label>
			</div>
			<!-- name -->
			<div class="form-group">
				<label for="name">שם</label>
				<input type="text" class="form-control" id="name" name="name" value={playlist.name} />
			</div>
			<!-- islands selection -->
			<div class="form-group">
				<IslandsManager {playlist} />
			</div>
			<button type="submit" class="btn btn-primary">שמור</button>

			<!-- <div class="form-group">
				<label for="start_at">התחל ב</label>
				<input
					type="datetime-local"
					class="form-control"
					id="start_at"
					name="start_at"
					value={playlist.start_at}
				/>
			</div>
			<div class="form-group">
				<label for="end_at">סיום ב</label>
				<input
					type="datetime-local"
					class="form-control"
					id="end_at"
					name="end_at"
					value={playlist.end_at}
				/>
			</div> -->
			<!-- assets -->
			<AssetsManager {playlist} />
		</form>
	</div>
{/if}
