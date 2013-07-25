#This file is part of activity module for Tryton. The COPYRIGHT file at
#the top level of this repository contains the full copyright notices and
#license terms.

from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


__metaclass__ = PoolMeta

__all__ = ['Activity']



class Activity:
    'Activity'
    __name__ = "activity.activity"

    calendar_event = fields.Many2One('calendar.event', 'Event')
    calendar = fields.Many2One('calendar.calendar', 'Calendar')

    @classmethod
    def __setup__(cls):
        super(Activity, cls).__setup__()
        cls._error_messages.update({
                'no_calendar_selected': ('Please select calendar for Activity '
                    ' %s before create an event'),
                'already_event': ('Activity %s has already and Event'),
                })

        cls._buttons.update({
                'create_calendar_event': {},
                })

    @classmethod
    @ModelView.button
    def create_calendar_event(cls, activities):
        Event = Pool().get('calendar.event')
        events = []
        for activity in activities:
            if activity.calendar_event:
                cls.raise_user_error('already_event',
                    (activity.rec_name,))
            if not activity.calendar:
                cls.raise_user_error('no_calendar_selected',
                    (activity.rec_name,))

            event = Event()
            event.dtstart = activity.dtstart
            event.dtend = activity.dtend
            event.calendar = activity.calendar.id
            event.summary = activity.subject
            event.description = activity.description
            event.save()

            activity.calendar_event=event
            activity.save()

