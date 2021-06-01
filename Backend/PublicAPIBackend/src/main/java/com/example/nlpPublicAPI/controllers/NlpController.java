package com.example.nlpPublicAPI.controllers;

import com.example.nlpPublicAPI.entities.Keywords;
import com.example.nlpPublicAPI.entities.Texts;
import com.example.nlpPublicAPI.services.NlpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NlpController {

    @Autowired
    NlpService nlpservice;

    @GetMapping("/")
    public String index(){
        System.out.println("Test");
        return "Hello";
    }

    //@GetMapping("/keywords")   just in case
    @GetMapping(value = "/keywords", produces = MediaType.APPLICATION_JSON_VALUE)
    public Keywords keywords(){
        //String kwords = nlpservice.getKeywords();
        return nlpservice.getKeywords();
    }

    //@GetMapping("/texts")
    @GetMapping(value = "/texts", produces = MediaType.APPLICATION_JSON_VALUE)
    public Texts texts(){
        //String texts = nlpservice.getTexts();
        return nlpservice.getTexts();
    }

}

