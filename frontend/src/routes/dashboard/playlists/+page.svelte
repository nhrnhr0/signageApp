<script>
	import AuthService from '$lib/auth';
	import PlaylistsService from '$lib/services/playlists';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import DashboardPaginator from '$lib/components/dashboard/DashboardPaginator.svelte';
	import DashboardSideFilters from '$lib/components/dashboard/DashboardSideFilters.svelte';
	import { goto } from '$app/navigation';
	import DashboardDataTable from '$lib/components/dashboard/DashboardDataTable.svelte';
	AuthService.protected_route();
	let resp = undefined;

	/** @type {import('$lib/types').Playlist[]} */
	let playlists = [];
	onMount(async () => {
		try {
			await refreshData();
		} catch (e) {
			console.error(e);
			playlists = [];
		}
	});

	/**
	 * Refresh the data from the server
	 * @param {string} query - The query string to send to the server
	 */
	async function refreshData(query = undefined) {
		try {
			resp = await PlaylistsService.getPlaylists(query || $page.url.search);
			playlists = resp.results;
		} catch (e) {
			console.error(e);
			playlists = [];
		}
	}

	/**
	 * Go to a specific page
	 * @param {CustomEvent} event - The event that triggered the function
	 */
	function goToPage(event) {
		let query = new URLSearchParams($page.url.searchParams.toString());
		query.set('page', event.detail.page);
		goto(`?${query.toString()}`);
		refreshData('?' + query.toString());
	}

	function update_filter(event) {
		let query = new URLSearchParams($page.url.searchParams.toString());
		for (let key of Object.keys(event.detail.query)) {
			query.set(key, event.detail.query[key]);
		}
		goto(`?${query.toString()}`);
		refreshData('?' + query.toString());
	}
</script>

<a href="/dashboard/playlists/new" class="btn btn-primary">צור פלייליסט חדש</a>
<h2 class="mb-4 mt-4">רשימת פלייליסטים</h2>
<div class="container-fluid">
	<div class="top-part">
		<input type="text" placeholder="Search..." />

		<div class="pagination">
			<DashboardPaginator
				count={resp?.count}
				next={resp?.next}
				previous={resp?.previous}
				current={$page.url.searchParams.get('page') || '1'}
				page_size={resp?.page_size || '5'}
				on:goToPage={goToPage}
			/>
		</div>
	</div>
	<div class="bottom-part">
		<div class="filters">
			<DashboardSideFilters
				filters={{
					is_active: {
						type: 'select',
						label: 'האם פעיל',
						url_key: 'is_active',
						options: [
							{ label: 'Active', value: 'true' },
							{ label: 'Inactive', value: 'false' },
							{ label: 'All', value: '' }
						],
						default: ''
					},
					page_size: {
						type: 'select',
						label: 'פריטים לעמוד',
						url_key: 'page_size',
						options: [
							{ label: '5', value: '5' },
							{ label: '10', value: '10' },
							{ label: '20', value: '20' }
						],
						default: '5'
					},
					created_at: {
						type: 'date_range',
						label: 'נוצר בתאריך',
						url_key: 'created_at'
					},
					updated_at: {
						type: 'date_range',
						label: 'עודכן בתאריך',
						url_key: 'updated_at'
					}
				}}
				on:filter={update_filter}
			/>
		</div>
		<div class="table">
			<DashboardDataTable
				{playlists}
				headers={[
					{
						label: 'מזהה',
						url_key: 'uuid',
						orderable: true,
						display: (playlist, header) => {
							return `<a href="/dashboard/playlists/${playlist.uuid}">${playlist.uuid.substring(0, 8)}</a>`;
						}
					},
					{
						label: 'שם',
						url_key: 'name',
						orderable: true,
						display: 'text'
					},
					{
						label: 'מספר תכנים',
						url_key: 'assets__count',
						orderable: true,
						display: 'number'
					},
					{
						label: 'האם פעיל',
						url_key: 'is_active',
						orderable: true,
						display: 'boolean'
					},
					{
						label: 'נוצר בתאריך',
						url_key: 'created_at',
						orderable: true,
						display: 'date'
					},
					{
						label: 'עודכן בתאריך',
						url_key: 'updated_at',
						orderable: true,
						display: 'date'
					}
				]}
			/>
		</div>
	</div>
</div>

<style lang="scss">
	.container-fluid {
		max-width: 1400px;
	}
	.top-part {
		display: flex;
		justify-content: space-between;
		flex-direction: column;
		margin-bottom: 30px;
	}

	.bottom-part {
		display: flex;
	}

	.filters {
		width: 20%;
		margin-left: 20px;
	}

	.table {
		width: 80%;
	}
</style>
