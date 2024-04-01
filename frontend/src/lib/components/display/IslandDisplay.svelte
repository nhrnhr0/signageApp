<script>
	import { fade } from 'svelte/transition';

	import { BACKEND_MEDIA_URL } from '$lib/consts';
	import { onMount } from 'svelte';
	import { is_schedual_active } from '$lib/utils';
	/**
	 * @type {import('$lib/types').Island|null}
	 */
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
		if (display_content.length === 0) {
			generate_display_content();
			setTimeout(next_asset, 5000);
			return;
		}
		let idx = (current_asset_index + 1) % display_content.length;

		// if we riched the start, we generate the display content again
		if (idx === 0) {
			generate_display_content();
			if (display_content.length === 0) {
				setTimeout(next_asset, 5000);
				return;
			}
		}

		current_asset_index = idx;
		if (display_content[idx].type === 'image') {
			clearTimeout(next_asset_timeout);
			next_asset_timeout = setTimeout(next_asset, display_content[idx].duration * 1000);
		} else if (display_content[idx].type === 'video') {
			clearTimeout(next_asset_timeout);
			if (display_content[idx].duration !== -1) {
				next_asset_timeout = setTimeout(next_asset, display_content[idx].duration * 1000);
			} else {
				// next when video ends
				setTimeout(() => {
					let vid = document.querySelector('video');
					if (vid) {
						// set video to play again
						vid.currentTime = 0;
						vid.play();
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
		next_asset();
	});

	function generate_display_content() {
		let _display_content = [];
		for (let i = 0; i < island.playlists.length; i++) {
			if (island.playlists[i].is_active === false) continue;
			if (island.playlists[i].schedule && !is_schedual_active(island.playlists[i].schedule))
				continue;

			for (let j = 0; j < island.playlists[i].assets.length; j++) {
				_display_content = _display_content.concat(island.playlists[i].assets[j]);
			}
		}
		// prefetch all the assets
		prefech_assets(display_content);
		display_content = _display_content;
		// console.log('updated display content ', island?.id, island?.name, display_content);
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
	{#each display_content as asset, i}
		<div
			class="asset"
			transition:fade
			style="display: {i === current_asset_index ? 'flex' : 'none'}"
		>
			{#if asset.type === 'video'}
				<video src="{BACKEND_MEDIA_URL}{asset.media}" autoplay muted loop={asset.duration !== -1}
				></video>
			{:else if asset.type === 'image'}
				<img src="{BACKEND_MEDIA_URL}{asset.media}" />
			{/if}
		</div>
	{/each}
{/if}

<style>
	.asset {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.asset img {
		height: 100%;
		width: 100%;
		max-width: 100%;
		max-height: 100%;

		object-fit: fill;
	}
	.asset video {
		height: 100%;
		width: 100%;
		max-width: 100%;
		max-height: 100%;

		object-fit: fill;
	}
</style>
