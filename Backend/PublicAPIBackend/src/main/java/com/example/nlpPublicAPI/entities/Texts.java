package com.example.nlpPublicAPI.entities;

public class Texts {

    int id;
    String documentlink;

    public Texts() {
    }

    public Texts(int id, String documentlink) {
        this.id = id;
        this.documentlink = documentlink;
    }

    public int getId() {
        return id;
    }

    public String getDocumentlink() {
        return documentlink;
    }

    @Override
    public String toString() {
        return "Texts{" +
                "id=" + id +
                ", documentlink='" + documentlink + '\'' +
                '}';
    }
}
