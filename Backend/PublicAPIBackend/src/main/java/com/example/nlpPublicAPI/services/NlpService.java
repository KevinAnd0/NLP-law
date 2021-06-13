package com.example.nlpPublicAPI.services;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class NlpService {

    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:1000/";

    public String searchTextByWord(String word) {
        String result = restTemplate.getForObject(url+"search/"+word, String.class);
        return result;
    }


}
