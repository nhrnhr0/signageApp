<script>
	import { fade } from 'svelte/transition';

	import { BACKEND_MEDIA_URL } from '$lib/consts';
	import { onMount } from 'svelte';

	export let island = null;
	/**
	 * @type {Array<{type: 'image' | 'video', media: string, duration: number}>}
	 */
	let display_content = [];
	let current_asset_index = -1;
	/**
     * @type {number}
     
     */
	let next_asset_timeout = 0;
	function next_asset() {
		if (display_content.length === 0) return;
		let idx = (current_asset_index + 1) % display_content.length;
		current_asset_index = idx;
		console.log(island.name + 'current_asset_index', current_asset_index, display_content);
		if (display_content[idx].type === 'image') {
			clearTimeout(next_asset_timeout);
			next_asset_timeout = setTimeout(next_asset, display_content[idx].duration * 1000);
		} else if (display_content[idx].type === 'video') {
			clearTimeout(next_asset_timeout);
			if (display_content[i].duration !== -1) {
				next_asset_timeout = setTimeout(next_asset, display_content[idx].duration * 1000);
			} else {
				// next when video ends
				setTimeout(() => {
					let vid = document.querySelector('video');
					if (vid) {
						vid.addEventListener('ended', next_asset);
					} else {
						next_asset();
					}
				}, 50);
				// if it's a video without a specific duration, we will wait for it to end and then move to the next asset
				// but if the video is stopped we will move to the next asset after 100 seconds
				next_asset_timeout = setTimeout(next_asset, 100 * 1000);
			}
		}
	}

	onMount(() => {
		generate_display_content();
		current_asset_index = -1;
		debugger;
		next_asset();
	});

	function generate_display_content() {
		let _display_content = [];

		for (let i = 0; i < island.playlists.length; i++) {
			for (let j = 0; j < island.playlists[i].assets.length; j++) {
				_display_content = _display_content.concat(island.playlists[i].assets[j]);
			}
		}
		// prefetch all the assets
		prefech_assets(display_content);
		display_content = _display_content;
	}
	function prefech_assets(display_content) {
		for (let i = 0; i < display_content.length; i++) {
			let asset = display_content[i];
			if (asset.type === 'video') {
				let video = new Video();
				video.src = asset.url;
			} else if (asset.type === 'image') {
				let img = new Image();
				img.src = asset.url;
			}
		}
	}
</script>

{#if island.playlists.length === 0}
	<p>אין תוכן להצגה</p>
{:else}
	<div class="asset-container">
		{#each display_content as asset, i}
			<!-- {#if i === current_asset_index} -->
			<div
				class="asset"
				transition:fade
				style="display: {i === current_asset_index ? 'flex' : 'none'}"
			>
				{#if asset.type === 'video'}
					<video src="{BACKEND_MEDIA_URL}{asset.media}" autoplay loop muted></video>
				{:else if asset.type === 'image'}
					<img src="{BACKEND_MEDIA_URL}{asset.media}" />
				{/if}
			</div>
			<!-- {/if} -->
		{/each}
	</div>
{/if}

<style>
	.asset-container {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.asset {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.asset img {
		max-width: 100%;
		max-height: 100%;
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
	.asset video {
		max-width: 100%;
		max-height: 100%;
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
</style>
