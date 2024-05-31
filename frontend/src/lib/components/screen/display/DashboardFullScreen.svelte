<script>
	import IconEdit from '$lib/components/icons/IconEdit.svelte';
	import playlists from '$lib/services/playlists';
	import { openModal } from 'svelte-modals';
	import EditPlaylistModal from '$lib/components/modals/EditPlaylistModal.svelte';
	import PlaylistSerice from '$lib/services/playlists';
	import AddOrCreatePlaylist from '../AddOrCreatePlaylist.svelte';
	import IconYes from '$lib/components/icons/IconYes.svelte';
	import IconNo from '$lib/components/icons/IconNo.svelte';
	import { onMount } from 'svelte';
	import { is_schedual_active } from '$lib/utils';
	export let screen;
	let all_options = [];
	function playlist_updated(playlist) {}
	function handle_edit_playlist_btn(playlist) {
		openModal(EditPlaylistModal, {
			playlist_uuid: playlist.uuid,
			onUpdated: playlist_updated
		});
	}

	async function loadOptions() {
		let resp = await PlaylistSerice.getPlaylists();
		debugger;
		let options = resp.results.map((playlist) => {
			return {
				uuid: playlist.uuid,
				name: playlist.name,
				is_active: playlist.is_active
			};
		});
		return options;
	}
	onMount(async () => {
		all_options = await loadOptions();
	});
</script>

<div class="wraper">
	<div class="row">
		<div class="col-12 item item-big">
			<div class="my-card">
				<div class="card-body">
					{#if screen}
						<p class="card-text">{screen.islands[0]?.name}:</p>
						<AddOrCreatePlaylist bind:island={screen.islands[0]} />
						<ul>
							{#each screen.islands[0].playlists as playlist}
								<li>
									<div>
										{playlist.name}
										<!-- is active  and is schedual active -->
										<small>
											{#if playlist.is_active && is_schedual_active(playlist.schedule)}
												<IconYes /> פעיל כרגע, ({playlist.assets__count} פריטים)
											{:else}
												<IconNo /> לא פעיל כרגע ({playlist.assets__count} פריטים)
											{/if}
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
											<small>
												<!-- remove btn -->
												<button
													type="button"
													class="btn btn-danger btn-sm"
													on:click={() => {
														let response = confirm('האם אתה בטוח שברצונך להסיר את הפלייליסט?');
														if (!response) return;
														screen.islands[0].playlists = screen.islands[0].playlists.filter(
															(p) => p.uuid !== playlist.uuid
														);
														screen = { ...screen };
													}}
												>
													הסר
												</button>
											</small>
										</small>
									</div>
								</li>
							{/each}
						</ul>
					{/if}
				</div>
			</div>
		</div>
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
