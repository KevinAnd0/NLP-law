package com.example.nlpPublicAPI.services;

import com.example.nlpPublicAPI.entities.Keywords;
import com.example.nlpPublicAPI.entities.Texts;
import com.fasterxml.jackson.databind.util.JSONPObject;
import org.apache.tomcat.util.json.JSONParser;
import org.springframework.boot.json.JsonParser;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;

@Service
public class NlpService {

    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:5000/";

    public Keywords getKeywords() {
        Keywords result = restTemplate.getForObject(url+"keywords", Keywords.class);
        return result;
    }

    public Texts getTexts() {
        Texts result = restTemplate.getForObject(url+"texts", Texts.class);
        return result;
    }


}
