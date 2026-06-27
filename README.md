# GamesGlitchlessStatic

## Serving: gzip for JSON changelogs

Enable gzip for the JSON changelog/index responses in the nginx vhost (the mod
`.jar/.zip` files are already compressed — do not gzip them):

```
gzip on;
gzip_types application/json;
gzip_min_length 1024;
```

Conditional GET (`ETag`/`If-None-Match` → `304`) is already supported by nginx's
default static handling; the launcher sends `If-None-Match` and caches the body.
