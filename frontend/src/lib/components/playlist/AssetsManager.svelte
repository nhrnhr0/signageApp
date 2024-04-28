<script>
	import ModalPlayListFileUpload from '../modals/ModalPlayListFileUpload.svelte';
	import { BACKEND_MEDIA_URL, BACKEND_URL } from '$lib/consts';
	import PlaylistService from '$lib/services/playlists';
	import { openModal } from 'svelte-modals';
	export let playlist;

	function upload_asset_btn() {
		// open the upload asset modal

		openModal(ModalPlayListFileUpload, {
			playlist: playlist,
			asset: null,
			open_file_browser: true,
			onUpdated: (_playlist) => {
				playlist = _playlist;
			}
		});
	}

	function edit_asset_btn(asset) {
		// open the upload asset modal
		openModal(ModalPlayListFileUpload, {
			playlist: playlist,
			asset: asset,
			open_file_browser: false,
			onUpdated: (_playlist) => {
				playlist = _playlist;
			}
		});
	}
</script>

<h2>תכנים</h2>
<div class="card-container">
	<!-- first item is a button designed like an item -->
	<div
		class="item"
		style="border: 2px dashed #000;cursor: pointer;"
		on:click|preventDefault={upload_asset_btn}
	>
		<div class="media-container">
			<img src="/icons8-upload-50_16x9.png" class="media-image" alt="upload" />
		</div>
		<div class="info" style="text-align: center;font-size: 1.5em;">
			<p>הוסף קובץ</p>
		</div>
	</div>

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
				<div class="sub-info">
					<p>{asset.duration} שניות</p>
					<p>
						<!-- Edit button btn -->
						<button
							class="btn btn-link"
							on:click|preventDefault={() => {
								edit_asset_btn(asset);
							}}>ערוך</button
						>
					</p>
				</div>
			</div>
		</div>

		<!-- display the name and duration -->
	{/each}
</div>

<!-- <button class="btn btn-primary" on:click|preventDefault={upload_asset_btn}> הוסף קובץ </button> -->

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

	.item .info .sub-info {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0px;
		margin: 0px;
	}
	.item .info .sub-info p {
		margin: 0px;
		padding: 0px;
	}

	.item .info .sub-info .btn-link {
		color: white;
		text-decoration: underline;
		cursor: pointer;
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
