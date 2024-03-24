<script>
	import IconEdit from '$lib/components/icons/IconEdit.svelte';
	import playlists from '$lib/services/playlists';
	import { openModal } from 'svelte-modals';
	import EditPlaylistModal from '$lib/components/modals/EditPlaylistModal.svelte';
	import PlaylistSerice from '$lib/services/playlists';
	import AddOrCreatePlaylist from '../AddOrCreatePlaylist.svelte';
	export let screen;
	function playlist_updated(playlist) {
		console.log('playlist_updated', playlist);
		screen = { ...screen };
	}
	function handle_edit_playlist_btn(playlist) {
		console.log('handle_edit_playlist_btn');
		openModal(EditPlaylistModal, {
			playlist_uuid: playlist.uuid,
			onUpdated: playlist_updated
		});
	}
</script>

<div class="wraper">
	<div class="row">
		<div class="col-12 item item-big">
			<div class="my-card">
				<div class="card-body">
					{#if screen}
						<p class="card-text">{screen.islands[0].name}:</p>
						<AddOrCreatePlaylist bind:island={screen.islands[0]} />
						<ul>
							{#each screen.islands[0].playlists as playlist}
								<li>
									<div>
										{playlist.name}
										<small>
											<a
												href="#"
												on:click={() => {
													handle_edit_playlist_btn(playlist);
												}}
											>
												<IconEdit />
											</a>
										</small>
									</div>
								</li>
							{/each}
						</ul>
					{/if}
				</div>
			</div>
		</div>
		<!-- 4 sub Items -->
		{#each screen?.islands.slice(1) as island}
			<div class="col-3 item item-small">
				<div class="my-card">
					<div class="card-body">
						<p class="card-text">
							{island.name}:
							<AddOrCreatePlaylist bind:island />
						</p>
						<ul>
							{#each island.playlists as playlist}
								<li>
									<div>
										{playlist.name}
										<small
											><a
												href="#"
												on:click={() => {
													handle_edit_playlist_btn(playlist);
												}}
											>
												<IconEdit /></a
											></small
										>
									</div>
								</li>
							{/each}
						</ul>
					</div>
				</div>
			</div>
		{/each}
	</div>
</div>

<style>
	/* big item 4/5 of the wraper's height */
	/* 4 subs each in 1/5 of the height and 1/4 of the width */
	.wraper {
		position: relative;
		/* padding-bottom: 80%; */
	}
	.wraper .row {
		/* position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%; */
	}
	.wraper .item {
		height: 100%;
		padding-left: 0px;
		padding-right: 0px;
	}
	.wraper .item-big {
	}
	.wraper .item-small {
	}
	.wraper .my-card {
		height: 100%;
		border: 1px solid #5555557e;
		border-radius: 10px;
	}
	.wraper .card-body {
		height: 100%;
	}
	.wraper .card-text {
		font-size: 1.5rem;
	}

	.wraper ul {
		overflow-y: auto;
		height: 100%;
	}
	.wraper ul li {
		margin-bottom: 10px;
	}
	.wraper ul li {
		font-size: 1.5rem;
	}
</style>
