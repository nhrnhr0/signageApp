<script>
	export let playlist;
	playlist.schedule;
	if (!playlist.schedule?.type) {
		playlist.schedule = {
			type: 'onOff',
			data: true
		};
	}
</script>

<select
	name="schedule-type"
	id="schedule-type"
	class="form-control"
	bind:value={playlist.schedule.type}
	on:change={() => {
		if (playlist.schedule.type === 'onOff') {
			playlist.schedule.data = true;
		} else if (playlist.schedule.type === 'betweenDates') {
			playlist.schedule.data = {
				start: '',
				end: ''
			};
		}
	}}
>
	<option value="onOff" selected>פעיל/לא פעיל</option>
	<option value="betweenDates">בין תאריכים</option>
</select>
<div class="wraper mt-4">
	{#if playlist.schedule.type === 'onOff'}
		<input
			type="checkbox"
			class="form-check-input"
			id="schedule-val"
			name="schedule-val"
			bind:checked={playlist.schedule.data}
		/>
		<label class="form-check-label" for="schedule-val">פעיל</label>
	{:else if playlist.schedule.type === 'betweenDates'}
		<label for="schedule-val-start">מתאריך</label>
		<input
			type="date"
			class="form-control"
			id="schedule-val-start"
			name="schedule-val-start"
			bind:value={playlist.schedule.data.start}
		/>
		<label for="schedule-val-end">עד תאריך</label>
		<input
			type="date"
			class="form-control"
			id="schedule-val-end"
			name="schedule-val-end"
			bind:value={playlist.schedule.data.end}
		/>
	{/if}
</div>

<style>
	.wraper {
		background-color: #f8f9fa;
		padding: 15px;
		border-radius: 5px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		margin: 25px;
	}
</style>
