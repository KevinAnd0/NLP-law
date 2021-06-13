package com.example.nlpPublicAPI.controllers;

import com.example.nlpPublicAPI.services.NlpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/api")
public class NlpController {

    @Autowired
    NlpService nlpservice;

    @GetMapping(value = "/search/{word}", produces = MediaType.APPLICATION_JSON_VALUE)
    public String search_words(@PathVariable String word){

        return nlpservice.searchTextByWord(word);
    }

}

