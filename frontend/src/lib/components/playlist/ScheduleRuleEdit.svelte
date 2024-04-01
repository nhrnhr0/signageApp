<script>
	import { SCHEDULE_RULE_TYPES, SCHEDULE_RULE_DICT, ScheduleRule } from '$lib/schedual/rule.js';
	import ScheduleRuleEdit from './ScheduleRuleEdit.svelte';
	export let rule;

	function rule_type_changed(e) {
		rule.type = e.target.value;
		// rule.sub_type = SCHEDULE_RULE_DICT[rule.type].sub_types[0].name;
		// rule.sub_rules = [];
		// the selected rule has sub types (so it's a date, time, or weekday rule)
		if (SCHEDULE_RULE_DICT[rule.type].sub_types.length) {
			// sett the rule default sub type
			rule.sub_type = SCHEDULE_RULE_DICT[rule.type].sub_types[0].name;
			// set the sub rules to an empty array
			rule.sub_rules = [];
		} else {
			// the selected rule has no sub types (so it's parent rule)
			// set the sub type to null
			rule.sub_type = null;
			// if the sub_rules array is empty, fill it with a default sub rule
			if (!rule.sub_rules || !rule.sub_rules.length) {
				rule.sub_rules = [new ScheduleRule()];
			}
		}

		reset_values();
	}

	function reset_values() {
		// if (rule.type == 'date') {
		// 	rule.value = { date: '' };
		// } else if (rule.type == 'time') {
		// 	rule.value = { date: '', start: '', end: '' };
		// } else if (rule.type == 'weekday') {
		// 	rule.value = { v1: false, v2: false, v3: false, v4: false, v5: false, v6: false, v7: false };
		// } else {
		// 	rule.value = {};
		// }
		rule.value = {};
	}
</script>

<div class="d-flex">
	<select name="rule" bind:value={rule.type} on:change={rule_type_changed} class="form-control">
		{#each SCHEDULE_RULE_TYPES as type}
			<option value={type.name}>{type.label}</option>
		{/each}
	</select>

	<!-- if the selected rule has sub types: meaning it's a date, time, or weekday rule -->
	{#if SCHEDULE_RULE_DICT[rule.type].sub_types.length}
		<select name="sub-type" bind:value={rule.sub_type} class="form-control">
			{#each SCHEDULE_RULE_DICT[rule.type].sub_types as sub_type}
				<option value={sub_type.name}>{sub_type.label}</option>
			{/each}
		</select>

		{#if rule.type == 'date'}
			{#if rule.sub_type == 'is_between'}
				<label for="start" class="form-label">מתאריך</label>
				<input type="date" bind:value={rule.value.start} id="start" class="form-control" />
				<label for="end" class="form-label">עד תאריך</label>
				<input type="date" bind:value={rule.value.end} id="end" class="form-control" />
			{:else}
				<input type="date" bind:value={rule.value.date} class="form-control" />
			{/if}
		{:else if rule.type == 'time'}
			{#if rule.sub_type == 'is_between'}
				<label for="start">משעה</label>
				<input type="time" bind:value={rule.value.start} id="start" />
				<label for="end">עד שעה</label>
				<input type="time" bind:value={rule.value.end} id="end" />
			{:else}
				<input type="time" bind:value={rule.value.date} />
			{/if}
		{:else if rule.type == 'weekday'}
			<!-- 7 checkboxes -->
			<!-- 
            ראשון, שני, שלישי, רביעי, חמישי, שישי, שבת
        -->
			<input
				type="checkbox"
				id="sunday"
				name="sunday"
				value="sunday"
				bind:checked={rule.value.v1}
			/>
			<label for="sunday">ראשון</label>
			<input
				type="checkbox"
				id="monday"
				name="monday"
				value="monday"
				bind:checked={rule.value.v2}
			/>
			<label for="monday">שני</label>
			<input
				type="checkbox"
				id="tuesday"
				name="tuesday"
				value="tuesday"
				bind:checked={rule.value.v3}
			/>
			<label for="tuesday">שלישי</label>
			<input
				type="checkbox"
				id="wednesday"
				name="wednesday"
				value="wednesday"
				bind:checked={rule.value.v4}
			/>
			<label for="wednesday">רביעי</label>
			<input
				type="checkbox"
				id="thursday"
				name="thursday"
				value="thursday"
				bind:checked={rule.value.v5}
			/>
			<label for="thursday">חמישי</label>
			<input
				type="checkbox"
				id="friday"
				name="friday"
				value="friday"
				bind:checked={rule.value.v6}
			/>
			<label for="friday">שישי</label>
			<input
				type="checkbox"
				id="saturday"
				name="saturday"
				value="saturday"
				bind:checked={rule.value.v7}
			/>
			<label for="saturday">שבת</label>
		{:else if rule.type == 'condition_any_of' || rule.type == 'condition_all_of'}{/if}
		<!-- {JSON.stringify(rule.value)} -->
	{/if}

	{#if rule.sub_rules && rule.sub_rules.length}
		<button
			type="button"
			on:click={() => (rule.sub_rules = [...rule.sub_rules, new ScheduleRule()])}
			class="btn btn-secondary btn-sm">הוסף תנאי</button
		>
	{/if}
</div>
{#if rule.sub_rules && rule.sub_rules.length}
	<div>
		<ul>
			{#if rule.sub_rules && rule.sub_rules.length}
				{#each rule.sub_rules as sub_rule}
					<li style="position: relative;">
						<button
							type="button"
							class="btn btn-danger btn-sm remove-btn"
							on:click={() => (rule.sub_rules = rule.sub_rules.filter((r) => r !== sub_rule))}
							>X</button
						>
						<ScheduleRuleEdit bind:rule={sub_rule} />
					</li>
				{/each}
			{/if}
		</ul>
	</div>
{/if}

<style>
	.form-control {
		margin: 5px 10px;

		width: auto;
	}
	.remove-btn {
		position: absolute;
		top: 0;
		right: 0;
		transform: translate(100%, 25%);
	}
</style>
