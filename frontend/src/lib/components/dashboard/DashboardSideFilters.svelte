<script>
	import { page } from '$app/stores';
	import { createEventDispatcher, onMount } from 'svelte';

	/** @type {Object} */
	export let filters = {};
	const dispatch = createEventDispatcher();
	let query = {};
	let loaded = false;
	onMount(() => {
		for (let key of Object.keys(filters)) {
			let key_url = filters[key].url_key;
			if (filters[key].type === 'select') {
				query[key_url] = $page.url.searchParams.get(key_url) || filters[key]?.default || '';
			} else if (filters[key].type === 'date_range') {
				let url_key_lte = `${key_url}__lte`;
				let url_key_gte = `${key_url}__gte`;
				query[url_key_lte] = $page.url.searchParams.get(url_key_lte) || '';
				query[url_key_gte] = $page.url.searchParams.get(url_key_gte) || '';
			}
		}
		loaded = true;
	});
	function filter_clicked() {
		dispatch('filter', { query });
	}

	function clear_query() {
		query = {};
		for (let key of Object.keys(filters)) {
			let key_url = filters[key].url_key;
			if (filters[key].type === 'select') {
				query[key_url] = filters[key]?.default || '';
			} else if (filters[key].type === 'date_range') {
				let url_key_lte = `${key_url}__lte`;
				let url_key_gte = `${key_url}__gte`;
				query[url_key_lte] = '';
				query[url_key_gte] = '';
			}
		}
	}
</script>

{#if !loaded}
	Loading...
{:else}
	<div class="dashboard-side-filters">
		{#each Object.keys(filters) as filter}
			<div class="filter">
				<label class="font-weight-bold mt-2">{filters[filter].label}</label> <br />
				{#if filters[filter].type === 'select'}
					<select class="form-select" bind:value={query[filters[filter].url_key]}>
						{#each filters[filter].options as option}
							<option
								value={option.value}
								selected={$page.url.searchParams.get(filters[filter].url_key) === option.value}
								>{option.label}</option
							>
						{/each}
					</select>
				{:else if filters[filter].type === 'date_range'}
					<div class="d-flex">
						<label for="">מ:&nbsp;&nbsp;</label>
						<input
							type="date"
							class="form-control"
							bind:value={query[`${filters[filter].url_key}__gte`]}
						/>
					</div>
					<div class="d-flex">
						<label for="">עד:</label>
						<input
							type="date"
							class="form-control"
							bind:value={query[`${filters[filter].url_key}__lte`]}
						/>
					</div>
				{/if}
			</div>
		{/each}

		<button class="btn btn-primary mt-3" on:click={filter_clicked}>סנן</button>
		<button
			class="btn btn-secondary mt-3"
			on:click={() => {
				clear_query();
				filter_clicked();
			}}
			>נקה מסננים
		</button>
	</div>
{/if}

<style>
	.dashboard-side-filters {
		display: flex;
		flex-direction: column;
	}
</style>
