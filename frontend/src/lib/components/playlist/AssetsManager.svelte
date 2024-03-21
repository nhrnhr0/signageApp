<script>
	import ModalPlayListFileUpload from '../modals/ModalPlayListFileUpload.svelte';
	import { BACKEND_MEDIA_URL, BACKEND_URL } from '$lib/consts';
	import PlaylistService from '$lib/network.js';
	import { openModal } from 'svelte-modals';
	export let playlist;

	function upload_asset_btn() {
		// open the upload asset modal
		console.log('upload_asset_btn');

		openModal(ModalPlayListFileUpload, {
			playlist: playlist,
			onAdded: (asset) => {
				playlist.assets.push(asset);
				playlist.assets = [...playlist.assets];
				console.log('onAdded', asset);
			}
		});
	}
</script>

<h2>תכנים</h2>

<div class="card-container">
	{#each playlist.assets as asset}
		<div class="item">
			<div class="media-container">
				{#if asset.type === 'image'}
					<img class="media-image" src={`${BACKEND_MEDIA_URL}${asset.media}`} alt={asset.name} />
				{:else if asset.type === 'video'}
					<video class="media-video" autoplay loop muted>
						<source src={`${BACKEND_MEDIA_URL}${asset.media}`} type="video/mp4" />
						Your browser does not support the video tag.
					</video>
				{/if}
			</div>
			<div class="info">
				<p>{asset.name}</p>
				<p>{asset.duration} שניות</p>
			</div>
		</div>

		<!-- display the name and duration -->
	{/each}
</div>
<button class="btn btn-primary" on:click|preventDefault={upload_asset_btn}> הוסף קובץ </button>

<style>
	.card-container {
		display: flex;
		flex-wrap: wrap;
		gap: 10px;
	}
	.item {
		width: 200px;
	}

	.item .info {
		display: flex;
		/* justify-content: space-between; */
		flex-direction: column;
		transform: translateY(-100%);
		background-color: rgba(0, 0, 0, 0.5);
		color: white;
	}

	.item .info p {
		margin: 0;

		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.media-container {
		position: relative;
		width: 100%;
		padding-bottom: 56.25%; /* 16:9 aspect ratio */
	}

	.media-image,
	.media-video {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}
</style>
