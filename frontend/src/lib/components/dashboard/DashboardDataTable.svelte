<!-- Data table -->
<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	/**
	 * @type {import('$lib/types').Playlist[]}
	 */
	export let playlists;

	/**
	 * @type {import('$lib/types').TableHeader[]}
	 */
	export let headers = []; //headers={[{label: 'מזהה',url_key: 'uuid',orderable: true,type: (playlist) => {return `<a href="/dashboard/playlists/${playlist.uuid}">${playlist.uuid}</a>`;}},{label: 'שם',url_key: 'name',orderable: true,type: 'text'},{label: 'מספר פריטים',url_key: 'assets__count',orderable: true,type: 'number'},{label: 'האם פעיל',url_key: 'is_active',orderable: true,type: 'boolean'},{label: 'נוצר בתאריך',url_key: 'created_at',orderable: true,type: 'date'},{label: 'עודכן בתאריך',url_key: 'updated_at',orderable: true,type: 'date'}]}
	let order_by = $page.url.searchParams.get('order_by') || undefined;
	/**
	 * @type {Object<string, import('$lib/types').TableHandlerFunction>}
	 */
	const handlers = {
		text: (playlist, header) => playlist[header.url_key],
		number: (playlist, header) => playlist[header.url_key],
		boolean: (playlist, header) => (playlist[header.url_key] ? 'כן' : 'לא'),
		date: (playlist, header) => new Date(playlist[header.url_key]).toLocaleDateString()
	};
</script>

<table>
	<thead>
		<tr>
			{#each headers as header}
				<th>{header.label}</th>
			{/each}
		</tr>
	</thead>
	<tbody>
		{#each playlists as playlist}
			<tr>
				{#each headers as header}
					{#if typeof header.display === 'function'}
						<td>{@html header.display(playlist, header)}</td>
					{:else}
						<td>{handlers[header.display](playlist, header)}</td>
					{/if}
				{/each}
			</tr>{/each}
	</tbody>
</table>

<style>
	table {
		width: 100%;
		border-collapse: collapse;
	}

	th,
	td {
		border: 1px solid #ddd;
		padding: 8px;
	}

	th {
		background-color: #f2f2f2;
	}

	tr:nth-child(even) {
		background-color: #f2f2f2;
	}

	tr:hover {
		background-color: #f2f2f2;
	}
</style>
