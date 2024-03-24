<script>
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import AuthService, { isLoggedIn } from '$lib/auth';
	import Spinner from '$lib/components/shared/Spinner.svelte';
	import { onMount } from 'svelte';
	import ScreenSerivce from '$lib/services/screens';
	import ScreenIslandsManager from '$lib/components/screen/ScreenIslandsManager.svelte';
	AuthService.protected_route();
	const uuid = $page.params.uuid;
	let screen = null;
	onMount(async () => {
		screen = await ScreenSerivce.getScreen(uuid);
	});
</script>

<!-- {
    "uuid": "ea273727-337f-4974-b3d3-9fac680bab4d",
    "name": "מסך 1",
    "is_active": true,
    "layout": "MainWith4Subs",
    "islands": [
        {
            "id": 2,
            "name": "Main",
            "playlists": [
                {
                    "uuid": "2014e976-43df-498d-b310-2826e1731545",
                    "name": "גנרי לכולם"
                }
            ]
        },
        {
            "id": 7,
            "name": "Sub1",
            "playlists": []
        },
        {
            "id": 8,
            "name": "Sub2",
            "playlists": []
        },
        {
            "id": 9,
            "name": "Sub3",
            "playlists": [
                {
                    "uuid": "2014e976-43df-498d-b310-2826e1731545",
                    "name": "גנרי לכולם"
                }
            ]
        },
        {
            "id": 10,
            "name": "Sub4",
            "playlists": []
        }
    ]
} -->
{#if screen === null}
	<Spinner />
{:else}
	<div class="container mt-5">
		<h2>מסך: {screen?.name}</h2>
		<h6>
			<a href="/display/{screen.code}" target="_blank">הצג במסך</a>
		</h6>
		<form action="" method="post" enctype="multipart/form-data">
			<!-- is_active -->
			<div class="form-group form-check">
				<input
					type="checkbox"
					class="form-check-input"
					id="is_active"
					name="is_active"
					checked={screen.is_active}
				/>
				<label class="form-check-label" for="is_active">פעיל</label>
			</div>
			<!-- name -->
			<div class="form-group">
				<label for="name">שם</label>
				<input type="text" class="form-control" id="name" name="name" value={screen.name} />
			</div>

			<!-- layout -->
			<div class="form-group">
				<label for="layout">תצוגה</label>
				<select class="form-control" id="layout" name="layout" value={screen.layout}>
					<option value="MainWith4Subs">ראשי עם 4 תתי תצוגה</option>
					<option value="FullScreen">מסך מלא</option>
				</select>
			</div>

			<!-- screen islands selection -->
			<div class="form-group">
				<ScreenIslandsManager {screen} />
			</div>
		</form>
	</div>

	<div class="container iframe-container mt-5">
		<h2>דמו</h2>
		<iframe src="/display/{screen.code}" width="100%" height="100%" frameborder="0" class="iframe"
		></iframe>
	</div>
{/if}

<style>
	.iframe-container {
		padding: 0px;
	}
	.iframe-container .iframe {
		aspect-ratio: 16 / 9;
		border: 1px solid black;
		width: 100%; /* change this to a fixed width, or create a container with a width. */
		height: 100%;
	}
</style>
