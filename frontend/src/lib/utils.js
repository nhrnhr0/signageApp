


export function is_schedual_active(schedual) {
    if (schedual === null)
    {
        return false;
    }
    if (schedual?.type === 'onOff')
    {
        return schedual?.data === true;
    } else if (schedual?.type === 'betweenDates')
    {
        const now = new Date();
        // if data.start is not set, we ignore start date
        // if data.end is not set, we ignore end date
        return (!schedual?.data?.start || new Date(schedual?.data?.start) <= now) && (!schedual?.data?.end || now <= new Date(schedual?.data?.end));
    }

}