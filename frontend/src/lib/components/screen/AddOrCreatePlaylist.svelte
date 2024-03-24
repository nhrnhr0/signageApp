<script>
	import Select from 'svelte-select';
	import PlaylistSerice from '$lib/services/playlists';
	import playlists from '$lib/services/playlists';
	import { openModal } from 'svelte-modals';
	import EditPlaylistModal from '$lib/components/modals/EditPlaylistModal.svelte';
	export let island;

	let options = [];
	async function loadOptions(filterText) {
		let resp = await PlaylistSerice.searchPlaylists(filterText);
		options = resp.map((playlist) => {
			return {
				uuid: playlist.uuid,
				name: playlist.name
			};
		});
		// filter out the playlists that are already in the island
		options = options.filter((option) => {
			return !island.playlists.some((playlist) => playlist.uuid === option.uuid);
		});
		return options;
	}
	function option_added(e) {
		let item = e.detail;
		island.playlists.push(item);
		island = { ...island };
	}
</script>

<div class="row">
	{#key island.playlists}
		<Select
			{loadOptions}
			placeholder="הוסף פלייליסט"
			on:change={(e) => option_added(e)}
			multiple={false}
			itemId="uuid"
		>
			<div slot="item" let:item let:index>{item.name}</div>
		</Select>
	{/key}
</div>
