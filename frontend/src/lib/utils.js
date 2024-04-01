
import { SCHEDULE_RULE_TYPES, SCHEDULE_RULE_DICT, ScheduleRule } from '$lib/schedual/rule.js';


export function is_schedual_active(schedual) {
    let root_rule = ScheduleRule.from_json(schedual);
    return root_rule.is_active();

}