// Prevent Firefox from continously dumping browser state(non incrementally) to session store file for crash recovery (affects SSD life)
// interval time in miliseconds
user_pref("browser.sessionstore.interval", 2700000);
user_pref("browser.sessionstore.interval.idle", 7200000);

// Use memory for caching insted of disk for performance and SSD life
user_pref("browser.cache.disk.enable", false);
user_pref("browser.cache.memory.enable", true);

// Stop Firefox from saving state data such as session cookies and form input to the session store (0=save for all sites, 1=save for http not https, 2=don't save) (for performance and SSD life)
user_pref("browser.sessionstore.privacy_level", 2);

// Reduce the number of closed tabs, closed windows, depth of back button history stored in the the session store
user_pref("browser.sessionstore.max_tabs_undo", 4);
user_pref("browser.sessionstore.max_windows_undo", 1);
user_pref("browser.sessionstore.max_serialize_back", 5);
user_pref("browser.sessionstore.cleanup.forget_closed_after", 900000);

// Disable telemetry archives
user_pref("toolkit.telemetry.archive.enabled", false);

// Enable Auto Update (Don't rely on package managers)
user_pref("app.update.auto", true);

