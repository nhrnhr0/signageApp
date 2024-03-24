<script>
	export let screen;

	function handle_edit_playlist_btn(playlist) {
		openModal(EditPlaylistModal, {
			playlist_uuid: playlist.uuid
		});
	}
</script>

<!-- show the one island inside the grid -->
<!-- make a 16/9 container -->
<div class="my-16-9">
	<div class="row">
		<div class="col-12 item">
			<div class="card">
				<div class="card-body">
					<p class="card-text">פלייליסטים:</p>
					<ul>
						{#each screen?.islands as island}
							{#each island.playlists as playlist}
								<li>
									<div>
										<a
											href="#"
											on:click={() => {
												handle_edit_playlist_btn(playlist);
											}}>{playlist.name}</a
										>
									</div>
								</li>
							{/each}
						{/each}
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.my-16-9 {
		position: relative;
		padding-bottom: 56.25%;
	}
	.my-16-9 .row {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}
	.my-16-9 .item {
		height: 100%;
	}
	.my-16-9 .card {
		height: 100%;
	}
	.my-16-9 .card-body {
		height: 100%;
	}
	.my-16-9 .card-text {
		font-size: 1.5rem;
	}
	.my-16-9 ul {
		overflow-y: auto;
		height: 100%;
	}
	.my-16-9 ul li {
		margin-bottom: 10px;
	}
	.my-16-9 ul li a {
		font-size: 1.5rem;
	}
</style>
