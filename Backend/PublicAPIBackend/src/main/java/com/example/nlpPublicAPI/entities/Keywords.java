package com.example.nlpPublicAPI.entities;

public class Keywords {

    int id;
    String keyword;

    public Keywords() {
    }

    public Keywords(int id, String keyword) {
        this.id = id;
        this.keyword = keyword;
    }

    public int getId() {
        return id;
    }

    public String getKeyword() {
        return keyword;
    }

    @Override
    public String toString() {
        return "Keywords{" +
                "id=" + id +
                ", keyword='" + keyword + '\'' +
                '}';
    }
}
