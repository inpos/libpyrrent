class plugin(object):
    pass

class alert_manager(object):
    operator = '(alert_manager const&)'
    m_mutex = None
    m_condition = None
    m_alert_mask = 0
    m_queue_size_limit = 0
    m_generation = 0
    m_alerts = []
    m_allocations = []
    def __init__(self, queue_limit, alert_mask = 'alert::error_notification'):      # XXX
        pass
    def emplace_alert(self, *args):
        '''
        mutex::scoped_lock lock(m_mutex);
        // don't add more than this number of alerts, unless it's a
        // high priority alert, in which case we try harder to deliver it
        // for high priority alerts, double the upper limit
        if (m_alerts[m_generation].size() >= m_queue_size_limit
            * (1 + T::priority))
            return;

        T alert(m_allocations[m_generation], std::forward<Args>(args)...);
        m_alerts[m_generation].push_back(alert);

        maybe_notify(&alert, lock);
'''
    def pending(self):
        pass
    def get_all(self, alerts):
        pass
    def should_post(self):
        '''
        mutex::scoped_lock lock(m_mutex);
        if (m_alerts[m_generation].size() >= m_queue_size_limit
            * (1 + T::priority))
        {
            return false;
        }
        return (m_alert_mask & T::static_category) != 0;
'''
    def wait_for_alert(self):
        pass
    def set_alert_mask(self, m):
        '''
        mutex::scoped_lock lock(m_mutex);
        m_alert_mask = m;
'''
    def alert_queue_size_limit(self):
        return m_queue_size_limit
    def set_alert_queue_size_limit(self, queue_size_limit_):
        pass
    def set_notify_function(self, fun):
        pass
    def maybe_notify(self):
        pass
    def m_notify(self):
        pass
    
    
    
    
    