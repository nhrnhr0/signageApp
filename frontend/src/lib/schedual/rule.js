// export const SCHEDULE_RULE_TYPES = ['date', 'time', 'weekday', 'condition_any_of', 'condition_all_of'];


export const SCHEDULE_RULE_TYPES = [{
    name: 'date',
    label: 'תאריך',
    sub_types: [
        {
            name: 'is_before_equal',
            label: 'החל מתאריך'

        },
        {
            name: 'is_after_equal',
            label: 'סיום בתאריך'
        },
        {
            name: 'is_between',
            label: 'בין התאריכים'
        }
    ]
}, {
    name: 'time',
    label: 'שעה',
    sub_types: [
        {
            name: 'is_before_equal',
            label: 'החל משעה'
        },
        {
            name: 'is_after_equal',
            label: 'סיום בשעה'
        },
        {
            name: 'is_between',
            label: 'בין השעות'
        }
    ]
}, {
    name: 'weekday',
    label: 'יום בשבוע',
    sub_types: [
        {
            name: 'is',
            label: 'הוא'
        },
        {
            name: 'is_not',
            label: 'אינו'
        }]
}, {
    name: 'condition_any_of',
    label: 'חלק מהתנאים',
    sub_types: []
}, {
    name: 'condition_all_of',
    label: 'כל התנאים',
    sub_types: []
}
];

export const SCHEDULE_RULE_DICT = SCHEDULE_RULE_TYPES.reduce((acc, type) => {
    acc[type.name] = type;
    return acc;
}, {});


export class ScheduleRule {
    /**
     * 
     * @param {string} type
     * @param {string} sub_type 
     * @param {Object} value 
     * @param {ScheduleRule[]} sub_rules 
     */
    constructor(type = 'date', sub_type = 'is_before_equal', value = {}, sub_rules = []) {
        this.type = type;
        this.sub_type = sub_type;
        /**
         * @type {ScheduleRule[]}
         */
        this.sub_rules = sub_rules || [];
        this.value = value;
    }
    /**
     * @param {JSON} json
     * @returns {ScheduleRule}
     */
    static from_json(json) {

        let rule = new ScheduleRule();
        rule.type = json?.type || 'date';
        rule.sub_type = json?.sub_type || 'is_before_equal';
        // var yesterday = new Date(Date.now() - 86400000);
        // format as "2024-04-27"
        rule.value = json?.value || { 'date': new Date().toISOString().split('T')[0] };

        let sub_rules = json?.sub_rules || [];
        rule.sub_rules = sub_rules.map((r) => ScheduleRule.from_json(r));
        return rule;
    }

    is_active(current_date = new Date()) {
        switch (this.type)
        {
            case 'date':
                return this.is_date_active(current_date);
            case 'time':
                return this.is_time_active(current_date);
            case 'weekday':
                return this.is_weekday_active(current_date);
            case 'condition_any_of':
                return this.is_condition_any_of_active(current_date);
            case 'condition_all_of':
                return this.is_condition_all_of_active(current_date);
        }
    }

    is_date_active(current_date) {
        let date = undefined;
        switch (this.sub_type)
        {

            case 'is_before_equal':
                date = new Date(this.value.date);
                return current_date >= date;
            case 'is_after_equal':
                date = new Date(this.value.date);
                return current_date <= date;
            case 'is_between':
                let start = new Date(this.value.start);
                let end = new Date(this.value.end);
                return current_date >= start && current_date <= end;
        }
    }

    is_time_active(current_date) {
        // let date = undefined;
        // let time = undefined;
        // let date = undefined;
        // switch (this.sub_type)
        // {
        //     case 'is_before_equal':
        //         time = moment(this.value, 'HH:mm');
        //         date = moment(current_date);
        //         date.set({ hour: time.hour(), minute: time.minute() });
        //         return date.isSameOrBefore(current_date);
        //         break;
        //     case 'is_after_equal':
        //         time = moment(this.value, 'HH:mm');
        //         date = moment(current_date);
        //         date.set({ hour: time.hour(), minute: time.minute() });
        //         return date.isSameOrAfter(current_date);
        //         break;
        //     case 'is_between':
        //         let start = moment(this.value.start, 'HH:mm');
        //         let end = moment(this.value.end, 'HH:mm');
        //         return moment(current_date).isBetween(start, end);
        // }
        // Parse current value based on comparison type
        let compareDate, compareStart, compareEnd;
        let comp_type = this.sub_type;
        let current_value = this.value;
        let hours, minutes;

        if (comp_type === 'is_before_equal' || comp_type === 'is_after_equal')
        {
            let val = current_value.date || '00:00';
            compareDate = new Date(current_date);
            [hours, minutes] = val.split(':');
            compareDate.setHours(hours, minutes, 0, 0);

        } else if (comp_type === 'is_between')
        {
            let val = current_value.start || '00:00';
            compareStart = new Date(current_date);
            [hours, minutes] = val.split(':');
            compareStart.setHours(hours, minutes, 0, 0);

            val = current_value.end || '23:59';
            compareEnd = new Date(current_date);
            [hours, minutes] = val.split(':');
            compareEnd.setHours(hours, minutes, 0, 0);
        } else
        {
            return false; // Invalid comparison type
        }

        // Compare datetime based on comp_type
        switch (comp_type)
        {
            case 'is_before_equal':
                return current_date >= compareDate;
            case 'is_after_equal':
                return current_date <= compareDate;
            case 'is_between':
                return current_date >= compareStart && current_date <= compareEnd;
            default:
                return false; // Invalid comparison type
        }
    }

    is_weekday_active(current_date) {
        let weekday = current_date.getDay() + 1; // 1-7
        // this.value = {v1:true, v3: true, v5: false}
        switch (this.sub_type)
        {
            case 'is':
                return this.value['v' + weekday];
            case 'is_not':
                return !this.value['v' + weekday];

        }
    }

    /**
     * 
     * @param {Date} current_date 
     * @returns {boolean}
     */
    is_condition_any_of_active(current_date) {
        return this.sub_rules.some((r) => r.is_active(current_date)) || this.sub_rules.length === 0;
    }

    /**
     * @param {Date} current_date
     * @returns {boolean}
     */
    is_condition_all_of_active(current_date) {
        return this.sub_rules.every((r) => r.is_active(current_date)) || this.sub_rules.length === 0;
    }



}