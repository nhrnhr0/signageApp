<script>
	import ScreensService from '$lib/services/screens';
	import { onMount } from 'svelte';
	import Select from 'svelte-select';
	let items = [];
	export let playlist;
	const groupBy = (item) => item.group;
	let selected_items = [];

	onMount(() => {
		ScreensService.getAllScreensAndIslands().then((data) => {
			items = data.map((screen) => {
				return screen.islands.map((island) => {
					return {
						label: screen.name + ' - ' + island.name,
						value: island.id,
						group: screen.name
					};
				});
			});
			items = items.flat();
			selected_items = items.filter((item) => {
				return (playlist.islands || []).some((island) => island.id === item.value);
			});
		});
	});
</script>

<Select
	placeholder="בחר מסכים"
	groupHeaderSelectable={false}
	searchable={true}
	multiple={true}
	{items}
	{groupBy}
	closeListOnChange={false}
	bind:value={selected_items}
	on:change={(e) => {
		playlist.islands = selected_items.map((item) => {
			return {
				id: item.value,
				name: item.label.split(' - ')[1]
			};
		});
	}}
	on:clear={(e) => {
		playlist.islands = selected_items.map((item) => {
			return {
				id: item.value,
				name: item.label.split(' - ')[1]
			};
		});
	}}
/>
