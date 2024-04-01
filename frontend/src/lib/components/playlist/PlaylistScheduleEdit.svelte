<script>
	import ScheduleRuleEdit from './ScheduleRuleEdit.svelte';
	import { ScheduleRule } from '$lib/schedual/rule.js';
	import { is_schedual_active } from '$lib/utils';
	export let playlist;
	playlist.schedule = ScheduleRule.from_json(playlist.schedule || {});
</script>

<div class="container form-group">
	<ScheduleRuleEdit bind:rule={playlist.schedule} />
</div>

{is_schedual_active(playlist.schedule)}
