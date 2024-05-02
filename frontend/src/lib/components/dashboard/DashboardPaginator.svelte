<script>
	import { createEventDispatcher } from 'svelte';
	export let count = ' ';
	export let next = null;
	export let previous = null;
	export let current = ' ';
	export let page_size;
	const dispatch = createEventDispatcher();
	function goToPage(page) {
		dispatch('goToPage', { page });
	}
</script>

<div class="dashboard-paginator">
	מציג דף {current} מתוך {Math.ceil(count / page_size)}<br /> סה"כ {count} פריטים
	<div class="actions">
		<button
			class="btn btn-primary"
			on:click={() => goToPage(parseInt(current) - 1)}
			disabled={previous === null}>קודם</button
		>
		<button
			class="btn btn-primary"
			on:click={() => goToPage(parseInt(current) + 1)}
			disabled={next === null}>הבא</button
		>
	</div>
</div>

<style>
	.dashboard-paginator {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.dashboard-paginator .actions {
		display: flex;
		padding-right: 10px;
	}
	.dashboard-paginator .actions button {
		margin-left: 10px;
	}
</style>
