package main

import (
    "encoding/json"
    "log"
    "net/http"
    "time"
)

func main() {
    http.HandleFunc("/", homeHandler)
    http.HandleFunc("/health", healthHandler)

    srv := &http.Server{
        Addr:         ":8080",
        ReadTimeout:  5 * time.Second,
        WriteTimeout: 10 * time.Second,
        IdleTimeout:  120 * time.Second,
    }

    log.Println("Server starting on :8080")
    if err := srv.ListenAndServe(); err != nil {
        log.Fatalf("Server failed: %v", err)
    }
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    w.WriteHeader(http.StatusOK)
    _, _ = w.Write([]byte(`<h1>Welcome to the Go App</h1><p>Healthy and running!</p>`))
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    resp := map[string]string{"status": "ok"}
    _ = json.NewEncoder(w).Encode(resp)
}
