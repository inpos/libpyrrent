from ..utils import Enum

class torrent_info(object):
    pass

class torrent_plugin(object):
    pass

class torrent_handle(object):
    pass

class add_torrent_params(object):
    flags_t = Enum({
                     'flag_seed_mode':      0x001,
                     'flag_upload_mode':    0x004,
                     'flag_share_mode':     0x008,
                     'flag_apply_ip_filter':        0x010,
                     'flag_paused':                 0x020,
                     'flag_auto_managed':           0x040,
                     'flag_duplicate_is_error':     0x080,
                     'flag_update_subscribe':       0x200,
                     'flag_super_seeding':          0x400,
                     'flag_sequential_download':    0x800,
                     'flag_pinned':                 0x2000,
                     'flag_stop_when_ready':        0x4000,
                     'flag_override_trackers':      0x8000,
                     'flag_override_web_seeds':     0x10000,
                     'flag_need_save_resume':       0x20000
                     })
    default_flags       = flags_t.flag_pinned | flags_t.flag_update_subscribe |\
                flags_t.flag_auto_managed | flags_t.flag_paused | flags_t.flag_apply_ip_filter |\
                flags_t.flag_need_save_resume
    version             = 0
    ti                  = None
    trackers            = []
    tracker_tiers       = []
    dht_nodes           = []
    name                = ''
    save_path           = ''
    storage_mode        = storage_mode_t
    storage             = storage_constructor_type
    userdata            = None
    file_priorities     = []
    extensions          = []
    trackerid           = ''
    url                 = ''
    flags               = 0
    info_hash           = None
    max_uploads         = 0
    max_connections     = 0
    upload_limit        = 0
    download_limit      = 0
    total_uploaded      = 0
    total_downloaded    = 0
    active_time         = 0
    finished_time       = 0
    seeding_time        = 0
    added_time          = 0
    completed_time      = 0
    last_seen_complete  = 0
    num_complete        = 0
    num_incomplete      = 0
    num_downloaded      = 0
    http_seeds          = []
    url_seeds           = []
    peers               = []
    banned_peers        = []
    unfinished_pieces   = []
    have_pieces         = []
    verified_pieces     = []
    piece_priorities    = []
    merkle_tree         = []
    renamed_files       = []
    
    def __init__(self,
                 version = LIBTORRENT_VERSION_NUM,
                 storage_mode = storage_mode_sparse,
                 storage = sc,
                 userdata = None,
                 flags = default_flags,
                 max_uploads = -1,
                 max_connections = -1,
                 upload_limit = -1,
                 download_limit = -1,
                 total_uploaded = 0,
                 total_downloaded = 0,
                 active_time = 0,
                 finished_time = 0,
                 seeding_time = 0,
                 added_time = 0,
                 completed_time = 0,
                 last_seen_complete = 0,
                 num_complete = -1,
                 num_incomplete = -1,
                 num_downloaded = -1):
        pass
    