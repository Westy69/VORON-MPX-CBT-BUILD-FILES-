





<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"  data-a11y-animated-images="system" data-a11y-link-underlines="false">

    <style>
  /* for each iteration, uncomment the CSS variable */

  /* light themes */
  [data-color-mode="light"][data-light-theme*="light"],
  [data-color-mode="auto"][data-light-theme*="light"] {
    /* iteration 1 */
    --border-color-iteration-1: #C8CCD0;
    /* iteration 2 */
    --border-color-iteration-2: #BABFC5;
    /* iteration 3 */
    --border-color-iteration-3: #A6ADB4;
    /* iteration final */
    --border-color-iteration-4: #868F99;

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  /* dark themes */
  [data-color-mode="dark"][data-dark-theme*="dark"],
  [data-color-mode="auto"][data-light-theme*="dark"] {
    /* iteration 1 */
    --border-color-iteration-1: #363940;
    /* iteration 2 */
    --border-color-iteration-2: #3F434B;
    /* iteration 3 */
    --border-color-iteration-3: #4B5159;
    /* iteration final */
    --border-color-iteration-4: #666E79;

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  [data-color-mode="dark"][data-dark-theme="dark_dimmed"],
  [data-color-mode="dark"][data-dark-theme="light_high_contrast"],
  [data-color-mode="dark"][data-dark-theme="dark_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_dimmed"],
  [data-color-mode="light"][data-light-theme="light_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_high_contrast"] {
    /* skip these themes, use the fallback */
    --control-borderColor-rest: initial !important;
  }

  @media (prefers-color-scheme: dark) {
    /* dark colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      --border-color-iteration-4: #666E79;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      --border-color-iteration-4: #868F99;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
      }

    [data-color-mode="auto"][data-dark-theme="dark_dimmed"],
    [data-color-mode="auto"][data-dark-theme="light_high_contrast"],
    [data-color-mode="auto"][data-dark-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }

  @media (prefers-color-scheme: light) {
    /* dark colors in light mode */
    [data-color-mode="auto"][data-light-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      --border-color-iteration-4: #666E79;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in light mode */
    [data-color-mode="auto"][data-light-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      --border-color-iteration-4: #868F99;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    [data-color-mode="auto"][data-light-theme="dark_dimmed"],
    [data-color-mode="auto"][data-light-theme="light_high_contrast"],
    [data-color-mode="auto"][data-light-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }
</style>


  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-b92e9647318f.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-5d486a4ede8e.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-27c8d635e4e5.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-8438e75afd36.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-bf5665b96628.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-c414b5ba1dce.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-e5868b7374db.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-299ac9c64ec0.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-3a26e78ad0ff.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-d6dcdf72e61d.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-faa25eb56e2e.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-de916a7feed5.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-71ecd5638fbf.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["copilot_conversational_ux_streaming","failbot_handle_non_errors","geojson_azure_maps","hovercard_show_on_focus","image_metric_tracking","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","star_button_focus"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-00c7b97f0987.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-56133143b228.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/environment-fc6543d75794.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-39506636d610.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-d14fe7eeba42.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-3485f2997bc6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-981cc2eaa259.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-add1ab03ecb3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-0a5a30c9b976.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_onfocus_ts-app_assets_modules_github_sticky-scroll-into-view_ts-c56a5dfc8975.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-7d50ad-9491f2be61ee.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-d77f85c54572.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-ba3118ed45b2.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-0104a8043aa4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-6bd50a0647d6.js"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-210c4b5934c3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-b8c027e1cfac.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Box_Box_js-96a44addc402.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_Button_js-node_modules_primer_react_lib-esm_-f6da63-1976b80d3486.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_js-03b6dd82d40a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_index_js-node_modules_primer_react_lib-esm_O-701f13-047a44a18d3a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-535c8ee1ebe8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-0f28951279b7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-2f08ef908241.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-04bb1b-a6096689d2d5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-9b048a5a5ceb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_react-router-dom_dist_index_js-4a785319b497.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-7693f4e3427d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-ad64b6-f3217651e114.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav2_index_js-b739f40cf454.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-9bd36c-c9a87fd5afd0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-6d3540-684005f5bdbe.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Breadcrumbs_Breadcrumbs_js-node_modules_primer_reac-31943d-f0539d68eb2b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-1ee1e572fd0e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_register-app_ts-afd2d748b726.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_ref-selector_RefSelector_tsx-bd2f6d26f4a6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-681869-f63e0555b81f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-cc11d2-cf61178576ab.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-388cefa74639.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-1cc1e433849f.js"></script>


  <title>klippain/scripts/system_info.py at main · Frix-x/klippain</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)">

    
  <meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7">


  <meta name="request-id" content="5D33:25B6B4:5BFBA2:63AB9C:652E435B" data-turbo-transient="true" /><meta name="html-safe-nonce" content="393f6f948898311252014340906d6b4608b923ebcec313273dafbfa1e2cb4168" data-turbo-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9Gcml4LXgva2xpcHBhaW4vdHJlZS9tYWluL3NjcmlwdHMiLCJyZXF1ZXN0X2lkIjoiNUQzMzoyNUI2QjQ6NUJGQkEyOjYzQUI5Qzo2NTJFNDM1QiIsInZpc2l0b3JfaWQiOiI3MDM0MTYxODg1NjE1NzM2NDI0IiwicmVnaW9uX2VkZ2UiOiJhdXN0cmFsaWFlYXN0IiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-turbo-transient="true" /><meta name="visitor-hmac" content="5b5cc040dda7ad2aa4d2ee2f5d69a832641d94a4b776a6974058172bf5dac6d2" data-turbo-transient="true" />


    <meta name="hovercard-subject-tag" content="repository:357818439" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
  <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" /><meta name="octolytics-actor-id" content="77569213" /><meta name="octolytics-actor-login" content="Westy69" /><meta name="octolytics-actor-hash" content="9f11da30d1b64b0bdd8adab976837633da2595ab33a03b44cb82b5865559854d" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




  

    <meta name="user-login" content="Westy69">

  <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="Generic Klipper configuration for 3D printers. Contribute to Frix-x/klippain development by creating an account on GitHub.">
      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/Frix-x/klippain/blob/main/scripts/system_info.py" />
      <meta name="twitter:image:src" content="https://repository-images.githubusercontent.com/357818439/adec8edb-e29a-435e-9e49-770e3386388b" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="klippain/scripts/system_info.py at main · Frix-x/klippain" /><meta name="twitter:description" content="Generic Klipper configuration for 3D printers. Contribute to Frix-x/klippain development by creating an account on GitHub." />
      <meta property="og:image" content="https://repository-images.githubusercontent.com/357818439/adec8edb-e29a-435e-9e49-770e3386388b" /><meta property="og:image:alt" content="Generic Klipper configuration for 3D printers. Contribute to Frix-x/klippain development by creating an account on GitHub." /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="klippain/scripts/system_info.py at main · Frix-x/klippain" /><meta property="og:url" content="https://github.com/Frix-x/klippain/blob/main/scripts/system_info.py" /><meta property="og:description" content="Generic Klipper configuration for 3D printers. Contribute to Frix-x/klippain development by creating an account on GitHub." />
      

      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/77569213/ws?session=eyJ2IjoiVjMiLCJ1Ijo3NzU2OTIxMywicyI6MTE2MjM3NTY5OSwiYyI6Mjg4MTU5MzU2NiwidCI6MTY5NzUzMDcyNX0=--ddae2d17a438acab598ba7b94206674db04812f5c4c1ebf34e8a8d967ec3e4c8" data-refresh-url="/_alive" data-session-id="e0dbdf0ceb6da4d661da91bbf0d74059cc8ab9566883517f250ccaa48efc14e1">
      <link rel="shared-web-socket-src" href="/assets-cdn/worker/socket-worker-cee473359cfe.js">


        <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="26301029d0481b645581b66f4f58c823ad9e1213ca445ff1a89a5d0295868fcd" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ee14a7165914197d62e19f664bfb961fcfdfc1ec31939a5c7b137fbab1751c87" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="1458c31d8d601dcb2e73daab09a2ba4225945457af895b170da96b350d467b17" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="e923129332abb6f03979d28ab39e347adc1232bd430795e7866ca8750415d3a2" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>
    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/Frix-x/klippain git https://github.com/Frix-x/klippain.git">

  <meta name="octolytics-dimension-user_id" content="10575621" /><meta name="octolytics-dimension-user_login" content="Frix-x" /><meta name="octolytics-dimension-repository_id" content="357818439" /><meta name="octolytics-dimension-repository_nwo" content="Frix-x/klippain" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="357818439" /><meta name="octolytics-dimension-repository_network_root_nwo" content="Frix-x/klippain" />



  <meta name="turbo-body-classes" content="logged-in env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
    <div data-turbo-body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


      

        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-b38cad-fb30c470f64b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-4db36910a4bc.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-00e5140a09e8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/command-palette-46bb1d1be80b.js"></script>

            <header class="AppHeader">
    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global">
  <include-fragment data-target="deferred-side-panel.fragment">
      
  <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534" id="dialog-show-dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-left" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534-title" aria-describedby="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-b447b111-22eb-4ec6-9b26-ed346c8e6534" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">    <div data-view-component="true" class="d-flex flex-column height-full mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-19caf707-dcac-47f4-b9c1-2467033e7d8c" href="/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-e35d4478-8f57-4e27-a590-9609573abaf8" href="/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-f87ea553-bba8-486f-9cad-fc813e59af28" href="/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-5829f426-10dd-4033-a2f7-97b76f53b5a4" href="/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-12d744e9-5c5e-4bb6-bd31-5ef65e54e5fb" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-e9c2afd0-9616-4fa4-87f2-a5ba887c064e" href="/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-268368a7-7d58-4b1c-9eda-1de9ca9bf8ae" href="/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</div>
</div>

      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">&copy; 2023 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex text-small text-light">
          <a target="_blank" href="/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="/security" data-view-component="true" class="Link mr-2">Security</a>
        <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>
</div></div>
</div>
      
</modal-dialog></div>

  </include-fragment>
</deferred-side-panel>

        <a
          class="AppHeader-logo ml-2"
          href="https://github.com/"
          data-hotkey="g d"
          aria-label="Homepage "
          data-turbo="false"
          data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
        >
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context" >
  <div class="AppHeader-context-compact">
        <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: Frix-x / klippain" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">    <span class="Button-content">
      <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">Frix-x</span>
                <span class="AppHeader-context-compact-separator">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate" >
  <span class="Truncate-text ">klippain</span>

</strong></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog role="dialog" id="context-region-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Frix-x&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/Frix-x" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          Frix-x
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;klippain&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/Frix-x/klippain" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          klippain
        </span>

</a>
    </li>
</ul>

</div>
      
</modal-dialog></div>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Frix-x&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/Frix-x/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/Frix-x" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          Frix-x
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;klippain&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="/Frix-x/klippain" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          klippain
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search" >
              


<qbsearch-input class="search-input" data-scope="repo:Frix-x/klippain" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="VD0JYd4-rCpmyb_RzYawkm-CZOc4mRQekYHQAlVgWavkFVAN7WEI4wQQdZhakXMbVQ9RiA_9tvK6XbnGapq9mg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="Frix-x/klippain" data-current-org="" data-current-owner="Frix-x" data-logged-in="true">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label
        for="AppHeader-searchInput"
        aria-label="Search or jump to…"
        class="AppHeader-search-visual--leading"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button
            type="button"
            data-target="qbsearch-input.inputButton"
            data-action="click:qbsearch-input#handleExpand"
            class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap"
            data-hotkey="s,/"
            data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}"
          >
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-e5320f9b-eece-4086-9549-69646181ed07" for="AppHeader-commandPalette-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-afd652d0-d1fb-4732-8bd2-5f8d23b3d63b" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          
  <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>  

      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

        <div class="position-relative">
                <ul
                  role="listbox"
                  class="ActionListWrap QueryBuilder-ListWrap"
                  aria-label="Suggestions"
                  data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  "
                  data-target="query-builder.resultsList"
                  data-persist-list=false
                  id="query-builder-test-results"
                ></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-afd652d0-d1fb-4732-8bd2-5f8d23b3d63b" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
                <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">    <span class="Button-content">
      <span class="Button-label">Give feedback</span>
    </span>
</button>  
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="jWXvYrawATIOsm3WSTG0QdjBk7zOJoOBvQX-cCf3diapn4LHkN7KV42B4ORZ-c9SnsbEmvkoW_0gFR-E3KRDGQ" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</modal-dialog></div>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="xbZZPJEmli0EB1gfzmCyRIIO5h8CGs5VsNPOXsNkaDDdjotzYnTj7HTYcO6iZz67SfnN8O01jm0lpTQkiBcKtw" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" value="_DWsVeGSR2BHpQtO11YqCpF8qW400V3bHvv9p6YlqhVGbAJ7p5NUy-SIDhuWB7A86vnoI7n2gyDZftmlviH2OQ" data-csrf="true" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</modal-dialog></div>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="dihrBU_zRdw5gbqfm21ov7JPVuSPVyJInmalUApTtpmgKDSQbabUSOLE4QXfiBaNLyePG9o6zizILD6vmUQrXg" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />

          </div>

        <div class="AppHeader-actions position-relative">
          <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <div data-view-component="true" class="Button-withTooltip">  <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted">    <span class="Button-content">
        <span class="Button-visual Button-leadingVisual">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
        </span>
      <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
    </span>
</button>  <tool-tip id="tooltip-6da03757-c780-4eab-af25-25cb50f289c6" for="global-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Create new...</tool-tip>
</div>

<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      
        <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new" tabindex="-1" id="item-729489d3-5e87-4ead-b5fc-7c41f6b16201" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new/import" tabindex="-1" id="item-33569761-ec07-4c43-abf5-f2812b206a39" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/codespaces/new" tabindex="-1" id="item-6eaa0820-6135-468a-ad0f-08271ca717b4" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-b8c6ca87-ff36-42d2-98d1-f6912d773199" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-2595a831-ed1c-4f4f-9d91-caf83efb5916" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div></anchored-position>  </focus-group>
</action-menu>

          <div data-view-component="true" class="Button-withTooltip">
  <a href="/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-94328f2a-272c-4606-bf6a-274bfc737600" aria-labelledby="tooltip-c86ded2a-7317-4aeb-9d5c-13581f1a1c8c" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-c86ded2a-7317-4aeb-9d5c-13581f1a1c8c" for="icon-button-94328f2a-272c-4606-bf6a-274bfc737600" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Issues</tool-tip>
</div>
          <div data-view-component="true" class="Button-withTooltip">
  <a href="/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-78b27fab-b1f4-48d2-ac70-425c3ea1e745" aria-labelledby="tooltip-d2c40a2a-b927-4c84-8d9c-dd1bd16d6d56" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-d2c40a2a-b927-4c84-8d9c-dd1bd16d6d56" for="icon-button-78b27fab-b1f4-48d2-ac70-425c3ea1e745" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Pull requests</tool-tip>
</div>

        </div>

        

<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6Nzc1NjkyMTMiLCJ0IjoxNjk3NTMwNzI1fQ==--30f10800aa1637e3c60d76bef243df61e1d97c5f6aa886af987acca10833a7ce" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel">
  <a id="AppHeader-notifications-button" href="/notifications"
    class="AppHeader-button Button--secondary"

    style="width:32px;height:32px;"

    data-hotkey="g n"
    data-target="notification-indicator.link"
    aria-label="Notifications"

      data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;notifications&quot;,&quot;label&quot;:null}"
  >

    <span
      data-target="notification-indicator.badge"
      class="mail-status unread d-none" hidden>
    </span>

      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox color-fg-muted mr-0">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
  </a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-98390ec7-7091-4f28-9821-8ca41a506d0a" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?memex_enabled=true&amp;repository=klippain&amp;user=Westy69&amp;user_can_create_organizations=true&amp;user_id=77569213">
  <include-fragment data-target="deferred-side-panel.fragment">
      <user-drawer-side-panel>
      <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb" id="dialog-show-dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">    <span class="Button-content">
      <span class="Button-label"><img src="https://avatars.githubusercontent.com/u/77569213?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" /></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-right" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb-title" aria-describedby="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="https://avatars.githubusercontent.com/u/77569213?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" />
</div>        <div data-view-component="true" class="overflow-hidden d-flex width-full">        <div data-view-component="true" class="lh-condensed overflow-hidden d-flex flex-column flex-justify-center ml-2 f5 mr-auto width-full">
          <span data-view-component="true" class="Truncate text-bold">
    <span data-view-component="true" class="Truncate-text">
            Westy69
</span>
</span>          </div>
</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-2d1e74d1-1254-4e56-87c2-124e0b36d8bb" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">    <div data-view-component="true" class="d-flex flex-column height-full mb-3">
        <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-49fbed81-4d73-4d06-821a-14faa0fdd3c5" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROFILE&quot;,&quot;label&quot;:null}" id="item-606b8ada-ecaf-45e5-b6f3-a6fdf8c322cd" href="https://github.com/Westy69" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-04d69b3e-9e0d-47dd-a26f-270d2e1d5f95" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;label&quot;:null}" id="item-91ff935d-e573-437d-bf70-fb39759b3004" href="/Westy69?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_PROJECTS&quot;,&quot;label&quot;:null}" id="item-b2a97115-cc93-45a7-812d-977f3965f1c4" href="/Westy69?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-860ff5cc-9dc2-452d-91c4-53f54c3c7a21" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_STARS&quot;,&quot;label&quot;:null}" id="item-22de0caf-0c13-44b6-9c10-37a0d1ae11f8" href="/Westy69?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SPONSORS&quot;,&quot;label&quot;:null}" id="item-460201f9-789c-456d-8001-c4967fe3349d" href="/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_GISTS&quot;,&quot;label&quot;:null}" id="item-203bedd4-42c7-4149-9202-a97edf4cc6e3" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-654c10aa-f09d-4e40-97a8-21e84af41c2d" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-3608ff1f-55f1-4809-806f-08b8474905a5" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-afa9beb5-33a9-4ff5-87fa-6a7cf6b657db" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SETTINGS&quot;,&quot;label&quot;:null}" id="item-f06dcd27-368c-49f0-b30d-28d80d00a047" href="/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DOCS&quot;,&quot;label&quot;:null}" id="item-6058e8d3-4fb5-4b78-bcdb-35476ab2bbc1" href="https://docs.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SUPPORT&quot;,&quot;label&quot;:null}" id="item-de732f61-de69-45b4-acae-92df63609059" href="https://support.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;LOGOUT&quot;,&quot;label&quot;:null}" id="item-73454217-90a7-4703-af30-2c47d820443e" href="/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
</div>
      
</modal-dialog></div>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu>

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar" >
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/Frix-x/klippain" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /Frix-x/klippain" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/Frix-x/klippain/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /Frix-x/klippain/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="24" data-view-component="true" class="Counter">24</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/Frix-x/klippain/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /Frix-x/klippain/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="9" data-view-component="true" class="Counter">9</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/Frix-x/klippain/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /Frix-x/klippain/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/Frix-x/klippain/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /Frix-x/klippain/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/Frix-x/klippain/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /Frix-x/klippain/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/Frix-x/klippain/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/Frix-x/klippain/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /Frix-x/klippain/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">        <details data-view-component="true" class="details-overlay details-reset position-relative">
    <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
    <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
          <ul>
              <li data-menu-item="i0code-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /Frix-x/klippain" href="/Frix-x/klippain">
                  Code
</a>              </li>
              <li data-menu-item="i1issues-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /Frix-x/klippain/issues" href="/Frix-x/klippain/issues">
                  Issues
</a>              </li>
              <li data-menu-item="i2pull-requests-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /Frix-x/klippain/pulls" href="/Frix-x/klippain/pulls">
                  Pull requests
</a>              </li>
              <li data-menu-item="i3actions-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /Frix-x/klippain/actions" href="/Frix-x/klippain/actions">
                  Actions
</a>              </li>
              <li data-menu-item="i4projects-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /Frix-x/klippain/projects" href="/Frix-x/klippain/projects">
                  Projects
</a>              </li>
              <li data-menu-item="i5security-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /Frix-x/klippain/security" href="/Frix-x/klippain/security">
                  Security
</a>              </li>
              <li data-menu-item="i6insights-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /Frix-x/klippain/pulse" href="/Frix-x/klippain/pulse">
                  Insights
</a>              </li>
          </ul>
</details-menu>
</details></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <div data-view-component="true" class="flash-close">
  <button id="icon-button-54199710-2b65-4f3f-a241-efdf97cb4720" aria-labelledby="tooltip-870c8a95-170d-4804-bd31-32852496a5ed" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium js-flash-close">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>  <tool-tip id="tooltip-870c8a95-170d-4804-bd31-32852496a5ed" for="icon-button-54199710-2b65-4f3f-a241-efdf97cb4720" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>
</div>

  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace>





  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div class="px-2" >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6Nzc1NjkyMTMiLCJ0IjoxNjk3NTMwNzI1fQ==--30f10800aa1637e3c60d76bef243df61e1d97c5f6aa886af987acca10833a7ce" data-view-component="true" class="js-socket-channel"></notification-shelf-watcher>
  <div hidden data-initial data-target="notification-shelf-watcher.placeholder"></div>






      <details
  class="details-reset details-overlay details-overlay-dark js-command-palette-dialog"
  id="command-palette-pjax-container"
  data-turbo-replace
>
  <summary aria-label="Command palette trigger" tabindex="-1"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="Command palette">
    <command-palette
      class="command-palette color-bg-default rounded-3 border color-shadow-small"
      return-to=/Frix-x/klippain/blob/main/scripts/system_info.py
      user-id="77569213"
      activation-hotkey="Mod+k,Mod+Alt+k"
      command-mode-hotkey="Mod+Shift+k"
      data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      ">

        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search issues and pull requests"
        ></command-palette-mode>
        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search issues, pull requests, discussions, and projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="!"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to a user, organization, or repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to a repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="/"
            data-scope-types="[&quot;repository&quot;]"
            data-placeholder="Search files"
        ></command-palette-mode>
        <command-palette-mode
          data-char="?"
        ></command-palette-mode>
        <command-palette-mode
          data-char="&gt;"
            data-placeholder="Run a command"
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
      <command-palette-mode
        class="js-command-palette-default-mode"
        data-char=""
        data-placeholder="Search or jump to..."
      ></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..."

        data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        "
      >
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden>
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle
              cx="8"
              cy="8"
              r="7"
              stroke="currentColor"
              stroke-opacity="0.25"
              stroke-width="2"
              vector-effect="non-scaling-stroke"
            ></circle>
            <path
              d="M15 8a7.002 7.002 0 00-7-7"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              vector-effect="non-scaling-stroke"
            ></path>
          </svg>
        </div>
        <command-palette-scope >
          <div data-target="command-palette-scope.placeholder" hidden class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token
                data-text="Frix-x"
                data-id="MDQ6VXNlcjEwNTc1NjIx"
                data-type="owner"
                data-value="Frix-x"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >Frix-x<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token
                data-text="klippain"
                data-id="MDEwOlJlcG9zaXRvcnkzNTc4MTg0Mzk="
                data-type="repository"
                data-value="klippain"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >klippain<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input
            class="js-overlay-input typeahead-input d-none"
            disabled
            tabindex="-1"
            aria-label="Hidden input for typeahead"
          >
          <input
            type="text"
            autocomplete="off"
            autocorrect="off"
            autocapitalize="off"
            spellcheck="false"
            class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator"
            aria-label="Command palette input"
            aria-haspopup="listbox"
            aria-expanded="false"
            aria-autocomplete="list"
            aria-controls="command-palette-page-stack"
            role="combobox"
            data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            "
          >
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-2ce50d28-0514-45d6-90ba-991905257c9a" for="command-palette-clear-button" popover="manual" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute">Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack
        data-default-scope-id="MDEwOlJlcG9zaXRvcnkzNTc4MTg0Mzk="
        data-default-scope-type="Repository"
        data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons"
      >
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error>
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty data-scope-types="*" data-match-mode="[^?]|^$">
          No results matched your search
        </command-palette-tip>

        <div hidden>

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group
              data-group-id="top"
              data-group-title="Top result"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="0"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="commands"
              data-group-title="Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}"
              data-default-priority="1"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="global_commands"
              data-group-title="Global Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}"
              data-default-priority="2"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="this_page"
              data-group-title="This Page"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="3"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="files"
              data-group-title="Files"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="4"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="default"
              data-group-title="Default"
              data-group-hint=""
              data-group-limits="{&quot;static_items_page&quot;:50}"
              data-default-priority="5"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="pages"
              data-group-title="Pages"
              data-group-hint=""
              data-group-limits="{&quot;repository&quot;:10}"
              data-default-priority="6"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="access_policies"
              data-group-title="Access Policies"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="7"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="organizations"
              data-group-title="Organizations"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="8"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="repositories"
              data-group-title="Repositories"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="9"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="references"
              data-group-title="Issues, pull requests, and discussions"
              data-group-hint="Type # to filter"
              data-group-limits="{}"
              data-default-priority="10"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="teams"
              data-group-title="Teams"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="11"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="users"
              data-group-title="Users"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="12"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="memex_projects"
              data-group-title="Projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="13"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="projects"
              data-group-title="Projects (classic)"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="14"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="footer"
              data-group-title="Footer"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="15"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="modes_help"
              data-group-title="Modes"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="16"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="filters_help"
              data-group-title="Use filters in issues, pull requests, discussions, and projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="17"
            >
            </command-palette-item-group>

            <command-palette-page
              data-page-title="Frix-x"
              data-scope-id="MDQ6VXNlcjEwNTc1NjIx"
              data-scope-type="owner"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
            <command-palette-page
              data-page-title="klippain"
              data-scope-id="MDEwOlJlcG9zaXRvcnkzNTc4MTg0Mzk="
              data-scope-type="repository"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
        </div>

        <command-palette-page data-is-root>
        </command-palette-page>
          <command-palette-page
            data-page-title="Frix-x"
            data-scope-id="MDQ6VXNlcjEwNTc1NjIx"
            data-scope-type="owner"
          >
          </command-palette-page>
          <command-palette-page
            data-page-title="klippain"
            data-scope-id="MDEwOlJlcG9zaXRvcnkzNTc4MTg0Mzk="
            data-scope-type="repository"
          >
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements"></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements">
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="@"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="!"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="/"
              data-scope-types="[&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="&gt;"
          >
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:pr"
          >
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:issue"
          >
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:discussion"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:project"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:open"
          >
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider
          data-type="commands"
          data-fetch-debounce="0"
            data-src="/command_palette/commands"
          data-supported-modes="[]"
            data-supports-commands
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_page_navigation"
          data-supported-modes="[&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to_members_only"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_members_only_prefetched"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="files"
          data-fetch-debounce="0"
            data-src="/command_palette/files"
          data-supported-modes="[&quot;/&quot;]"
            data-supported-scope-types="[&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/discussions"
          data-supported-modes="[&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/projects"
          data-supported-modes="[&quot;#&quot;,&quot;!&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/recent_issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/teams"
          data-supported-modes="[&quot;@&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/name_with_owner_repository"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
    </command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path
          fill="#959da5"
          d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"
        />
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      
      






    
  <div id="repository-container-header" data-turbo-replace hidden></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Alt+Meta+≥,Control+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Alt+Meta+≤,Control+Alt+," target="_blank" href="/codespaces/new/Frix-x/klippain/tree/main?resume=1">Open in codespace</a>



    
      
    





<react-app
  app-name="react-code-view"
  initial-path="/Frix-x/klippain/blob/main/scripts/system_info.py"
  style="min-height: calc(100vh - 62px)"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"scripts":{"items":[{"name":"gcode_shell_command.py","path":"scripts/gcode_shell_command.py","contentType":"file"},{"name":"graph_vibrations.py","path":"scripts/graph_vibrations.py","contentType":"file"},{"name":"plot_graphs.sh","path":"scripts/plot_graphs.sh","contentType":"file"},{"name":"shell_commands.cfg","path":"scripts/shell_commands.cfg","contentType":"file"},{"name":"system_info.py","path":"scripts/system_info.py","contentType":"file"}],"totalCount":5},"":{"items":[{"name":".github","path":".github","contentType":"directory"},{"name":"adxl_results","path":"adxl_results","contentType":"directory"},{"name":"config","path":"config","contentType":"directory"},{"name":"docs","path":"docs","contentType":"directory"},{"name":"macros","path":"macros","contentType":"directory"},{"name":"moonraker","path":"moonraker","contentType":"directory"},{"name":"scripts","path":"scripts","contentType":"directory"},{"name":"user_templates","path":"user_templates","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"install.sh","path":"install.sh","contentType":"file"}],"totalCount":12}},"fileTreeProcessingTime":5.785893000000001,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":357818439,"defaultBranch":"main","name":"klippain","ownerLogin":"Frix-x","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2021-04-14T19:44:24.000+12:00","ownerAvatar":"https://avatars.githubusercontent.com/u/10575621?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1697491037.0","canEdit":true,"refType":"branch","currentOid":"b49bcbfbca968a8b633fe6f0b21618365be04a4a"},"path":"scripts/system_info.py","currentUser":{"id":77569213,"login":"Westy69","userEmail":"rent2ownnz@gmail.com"},"blob":{"rawLines":["#!/usr/bin/env python3","","######################################","###### BASIC SYSTEM INFO SCRIPT ######","######################################","# Written by Frix_x#0161 #","# @version: 1.0","","# CHANGELOG:","#   v1.0: first version of the script to get some system info printed in the klippy.log","","","# Be sure to make this script executable using SSH: type 'chmod +x ./system_info.py' when in the folder !","","#####################################################################","################ !!! DO NOT EDIT BELOW THIS LINE !!! ################","#####################################################################","","import subprocess","import os","import platform","from datetime import datetime","import concurrent.futures","","def get_date_time():","    # Special note for power-user running Klipper inside a docker container: usually the timezone","    # is not set and this result in a print of the UTC time (instead of local). Consider running","    # the container like: \"docker run -e TZ=America/New_York klipper_image\"","    # in order to get a proper timezone set and get the correct time read by this script","    return datetime.now().strftime(\"%m/%d/%Y, %H:%M:%S\")","","def check_docker():","    return os.path.exists('/.dockerenv')","","def check_wsl():","    try:","        with open('/proc/version', 'r') as f:","            if 'microsoft' in f.read().lower():","                return True","    except Exception:","        pass","    return False","","def get_pi_model():","    try:","        model_info = subprocess.check_output(['cat', '/sys/firmware/devicetree/base/model'], universal_newlines=True)","        if 'raspberry pi' in model_info.lower(): return model_info","    except subprocess.CalledProcessError:","        return None","    else:","        return None","","def get_unknown_board_info():","    try:","        with open('/proc/cpuinfo', 'r') as f:","            for line in f:","                if line.startswith('Hardware') or line.startswith('Model'):","                    return line.split(':')[1].strip()","        with open('/etc/os-release', 'r') as f:","            for line in f:","                if line.startswith('PRETTY_NAME') or line.startswith('NAME'):","                    return line.split('=')[1].strip().strip('\"')","    except Exception:","        pass","","    return \"no additional info...\"","","def get_os_kernel_info():","    uname = os.uname()","    return uname.sysname, uname.release, uname.machine","","def get_ram_info():","    try:","        total_ram = subprocess.check_output(['free', '-m'], universal_newlines=True).split('\\n')[1].split()[1]","        available_ram = subprocess.check_output(['free', '-m'], universal_newlines=True).split('\\n')[1].split()[6]","        return total_ram, available_ram","    except subprocess.CalledProcessError:","        return None, None","","","def print_system_info():","    with concurrent.futures.ThreadPoolExecutor() as executor:","        future_date_time = executor.submit(get_date_time)","        future_docker = executor.submit(check_docker)","        future_pi_model = executor.submit(get_pi_model)","        future_wsl = executor.submit(check_wsl)","        future_os_kernel = executor.submit(get_os_kernel_info)","        future_ram_info = executor.submit(get_ram_info)","","","    date_time = future_date_time.result()","    print(f\"Klippain started ({date_time})\")","","    sysname, release, machine = future_os_kernel.result()","    print(f\"Operating System: {sysname} - {release}\")","","","    is_docker = future_docker.result()","    is_wsl = future_wsl.result()","    pi_model = future_pi_model.result()","","    if is_docker:","        print(f\"Machine: {machine} - in a docker container\")","    elif is_wsl:","        print(f\"Machine: {machine} - in Windows Subsystem for Linux\")","    elif pi_model is not None:","        print(f\"Machine: {machine} - in a {pi_model}\")","    else:","        # This is the case where it is running on a unknown machine type","        # so we use the specific function to try to gather more info...","        print(f\"Machine: {machine}\")","        print(f\"System information: {get_unknown_board_info()}\")","","","    total_ram, available_ram = future_ram_info.result()","    if total_ram is None or available_ram is None:","        print(\"RAM information not found...\")","    else:","        print(f\"Used RAM: {available_ram}/{total_ram} MB\")","","","if __name__ == \"__main__\":","    print_system_info()"],"stylingDirectives":[[{"start":0,"end":22,"cssClass":"pl-c"}],[],[{"start":0,"end":38,"cssClass":"pl-c"}],[{"start":0,"end":38,"cssClass":"pl-c"}],[{"start":0,"end":38,"cssClass":"pl-c"}],[{"start":0,"end":26,"cssClass":"pl-c"}],[{"start":0,"end":15,"cssClass":"pl-c"}],[],[{"start":0,"end":12,"cssClass":"pl-c"}],[{"start":0,"end":87,"cssClass":"pl-c"}],[],[],[{"start":0,"end":105,"cssClass":"pl-c"}],[],[{"start":0,"end":69,"cssClass":"pl-c"}],[{"start":0,"end":69,"cssClass":"pl-c"}],[{"start":0,"end":69,"cssClass":"pl-c"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":17,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":9,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":20,"cssClass":"pl-k"},{"start":21,"end":29,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":17,"cssClass":"pl-s1"},{"start":18,"end":25,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":17,"cssClass":"pl-en"}],[{"start":4,"end":97,"cssClass":"pl-c"}],[{"start":4,"end":96,"cssClass":"pl-c"}],[{"start":4,"end":75,"cssClass":"pl-c"}],[{"start":4,"end":88,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-en"},{"start":35,"end":55,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":16,"cssClass":"pl-en"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":19,"end":25,"cssClass":"pl-en"},{"start":26,"end":39,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":13,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-k"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-en"},{"start":18,"end":33,"cssClass":"pl-s"},{"start":35,"end":38,"cssClass":"pl-s"},{"start":40,"end":42,"cssClass":"pl-k"},{"start":43,"end":44,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-en"},{"start":39,"end":44,"cssClass":"pl-en"}],[{"start":16,"end":22,"cssClass":"pl-k"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-c1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":16,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-k"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":31,"cssClass":"pl-s1"},{"start":32,"end":44,"cssClass":"pl-en"},{"start":46,"end":51,"cssClass":"pl-s"},{"start":53,"end":90,"cssClass":"pl-s"},{"start":93,"end":111,"cssClass":"pl-s1"},{"start":111,"end":112,"cssClass":"pl-c1"},{"start":112,"end":116,"cssClass":"pl-c1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":25,"cssClass":"pl-s"},{"start":26,"end":28,"cssClass":"pl-c1"},{"start":29,"end":39,"cssClass":"pl-s1"},{"start":40,"end":45,"cssClass":"pl-en"},{"start":49,"end":55,"cssClass":"pl-k"},{"start":56,"end":66,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":21,"cssClass":"pl-s1"},{"start":22,"end":40,"cssClass":"pl-v"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-c1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":26,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-k"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-en"},{"start":18,"end":33,"cssClass":"pl-s"},{"start":35,"end":38,"cssClass":"pl-s"},{"start":40,"end":42,"cssClass":"pl-k"},{"start":43,"end":44,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":34,"cssClass":"pl-en"},{"start":35,"end":45,"cssClass":"pl-s"},{"start":47,"end":49,"cssClass":"pl-c1"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":65,"cssClass":"pl-en"},{"start":66,"end":73,"cssClass":"pl-s"}],[{"start":20,"end":26,"cssClass":"pl-k"},{"start":27,"end":31,"cssClass":"pl-s1"},{"start":32,"end":37,"cssClass":"pl-en"},{"start":38,"end":41,"cssClass":"pl-s"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":51,"cssClass":"pl-en"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-en"},{"start":18,"end":35,"cssClass":"pl-s"},{"start":37,"end":40,"cssClass":"pl-s"},{"start":42,"end":44,"cssClass":"pl-k"},{"start":45,"end":46,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":34,"cssClass":"pl-en"},{"start":35,"end":48,"cssClass":"pl-s"},{"start":50,"end":52,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-s1"},{"start":58,"end":68,"cssClass":"pl-en"},{"start":69,"end":75,"cssClass":"pl-s"}],[{"start":20,"end":26,"cssClass":"pl-k"},{"start":27,"end":31,"cssClass":"pl-s1"},{"start":32,"end":37,"cssClass":"pl-en"},{"start":38,"end":41,"cssClass":"pl-s"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":51,"cssClass":"pl-en"},{"start":54,"end":59,"cssClass":"pl-en"},{"start":60,"end":63,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":34,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":22,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":14,"cssClass":"pl-s1"},{"start":15,"end":20,"cssClass":"pl-en"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":24,"cssClass":"pl-s1"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":32,"end":39,"cssClass":"pl-s1"},{"start":41,"end":46,"cssClass":"pl-s1"},{"start":47,"end":54,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":16,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-k"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":30,"cssClass":"pl-s1"},{"start":31,"end":43,"cssClass":"pl-en"},{"start":45,"end":51,"cssClass":"pl-s"},{"start":53,"end":57,"cssClass":"pl-s"},{"start":60,"end":78,"cssClass":"pl-s1"},{"start":78,"end":79,"cssClass":"pl-c1"},{"start":79,"end":83,"cssClass":"pl-c1"},{"start":85,"end":90,"cssClass":"pl-en"},{"start":91,"end":95,"cssClass":"pl-s"},{"start":92,"end":94,"cssClass":"pl-cce"},{"start":97,"end":98,"cssClass":"pl-c1"},{"start":100,"end":105,"cssClass":"pl-en"},{"start":108,"end":109,"cssClass":"pl-c1"}],[{"start":8,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":34,"cssClass":"pl-s1"},{"start":35,"end":47,"cssClass":"pl-en"},{"start":49,"end":55,"cssClass":"pl-s"},{"start":57,"end":61,"cssClass":"pl-s"},{"start":64,"end":82,"cssClass":"pl-s1"},{"start":82,"end":83,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":94,"cssClass":"pl-en"},{"start":95,"end":99,"cssClass":"pl-s"},{"start":96,"end":98,"cssClass":"pl-cce"},{"start":101,"end":102,"cssClass":"pl-c1"},{"start":104,"end":109,"cssClass":"pl-en"},{"start":112,"end":113,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":24,"cssClass":"pl-s1"},{"start":26,"end":39,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":21,"cssClass":"pl-s1"},{"start":22,"end":40,"cssClass":"pl-v"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":21,"cssClass":"pl-en"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":19,"cssClass":"pl-s1"},{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":46,"cssClass":"pl-v"},{"start":49,"end":51,"cssClass":"pl-k"},{"start":52,"end":60,"cssClass":"pl-s1"}],[{"start":8,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":35,"cssClass":"pl-s1"},{"start":36,"end":42,"cssClass":"pl-en"},{"start":43,"end":56,"cssClass":"pl-s1"}],[{"start":8,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-s1"},{"start":33,"end":39,"cssClass":"pl-en"},{"start":40,"end":52,"cssClass":"pl-s1"}],[{"start":8,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-en"},{"start":42,"end":54,"cssClass":"pl-s1"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":29,"cssClass":"pl-s1"},{"start":30,"end":36,"cssClass":"pl-en"},{"start":37,"end":46,"cssClass":"pl-s1"}],[{"start":8,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":35,"cssClass":"pl-s1"},{"start":36,"end":42,"cssClass":"pl-en"},{"start":43,"end":61,"cssClass":"pl-s1"}],[{"start":8,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-en"},{"start":42,"end":54,"cssClass":"pl-s1"}],[],[],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":32,"cssClass":"pl-s1"},{"start":33,"end":39,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":43,"cssClass":"pl-s"},{"start":30,"end":41,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-kos"},{"start":31,"end":40,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"}],[],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":22,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":48,"cssClass":"pl-s1"},{"start":49,"end":55,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":52,"cssClass":"pl-s"},{"start":30,"end":39,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-kos"},{"start":31,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-kos"},{"start":42,"end":51,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-kos"},{"start":43,"end":50,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-kos"}],[],[],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":29,"cssClass":"pl-s1"},{"start":30,"end":36,"cssClass":"pl-en"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-en"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-en"}],[],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":16,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":59,"cssClass":"pl-s"},{"start":25,"end":34,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-kos"},{"start":26,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-kos"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":15,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":68,"cssClass":"pl-s"},{"start":25,"end":34,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-kos"},{"start":26,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-kos"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":24,"cssClass":"pl-c1"},{"start":25,"end":29,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":53,"cssClass":"pl-s"},{"start":25,"end":34,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-kos"},{"start":26,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-kos"},{"start":42,"end":52,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-kos"},{"start":43,"end":51,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-kos"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":72,"cssClass":"pl-c"}],[{"start":8,"end":71,"cssClass":"pl-c"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":35,"cssClass":"pl-s"},{"start":25,"end":34,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-kos"},{"start":26,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-kos"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":63,"cssClass":"pl-s"},{"start":36,"end":62,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-kos"},{"start":37,"end":59,"cssClass":"pl-en"},{"start":61,"end":62,"cssClass":"pl-kos"}],[],[],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":15,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":31,"end":46,"cssClass":"pl-s1"},{"start":47,"end":53,"cssClass":"pl-en"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-c1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":41,"cssClass":"pl-s1"},{"start":42,"end":44,"cssClass":"pl-c1"},{"start":45,"end":49,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":44,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":57,"cssClass":"pl-s"},{"start":26,"end":41,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-kos"},{"start":27,"end":40,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"},{"start":42,"end":53,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-kos"},{"start":43,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-kos"}],[],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":21,"cssClass":"pl-en"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Frix-x/klippain/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/Frix-x/klippain/security/dependabot","repoSecurityAndAnalysisPath":"/Frix-x/klippain/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"system_info.py","displayUrl":"https://github.com/Frix-x/klippain/blob/main/scripts/system_info.py?raw=true","headerInfo":{"blobSize":"4.14 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"1995944","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FFrix-x%2Fklippain%2Fblob%2Fmain%2Fscripts%2Fsystem_info.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"123","truncatedSloc":"97"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/Frix-x/klippain/discussions/new","newIssuePath":"/Frix-x/klippain/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Frix-x/klippain/blob/main/scripts/system_info.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/Frix-x/klippain/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/Frix-x/klippain/raw/main/scripts/system_info.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Frix-x","repoName":"klippain","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"get_date_time","kind":"function","ident_start":711,"ident_end":724,"extent_start":707,"extent_end":1144,"fully_qualified_name":"get_date_time","ident_utf16":{"start":{"line_number":24,"utf16_col":4},"end":{"line_number":24,"utf16_col":17}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":29,"utf16_col":56}}},{"name":"check_docker","kind":"function","ident_start":1150,"ident_end":1162,"extent_start":1146,"extent_end":1206,"fully_qualified_name":"check_docker","ident_utf16":{"start":{"line_number":31,"utf16_col":4},"end":{"line_number":31,"utf16_col":16}},"extent_utf16":{"start":{"line_number":31,"utf16_col":0},"end":{"line_number":32,"utf16_col":40}}},{"name":"check_wsl","kind":"function","ident_start":1212,"ident_end":1221,"extent_start":1208,"extent_end":1407,"fully_qualified_name":"check_wsl","ident_utf16":{"start":{"line_number":34,"utf16_col":4},"end":{"line_number":34,"utf16_col":13}},"extent_utf16":{"start":{"line_number":34,"utf16_col":0},"end":{"line_number":41,"utf16_col":16}}},{"name":"get_pi_model","kind":"function","ident_start":1413,"ident_end":1425,"extent_start":1409,"extent_end":1714,"fully_qualified_name":"get_pi_model","ident_utf16":{"start":{"line_number":43,"utf16_col":4},"end":{"line_number":43,"utf16_col":16}},"extent_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":50,"utf16_col":19}}},{"name":"get_unknown_board_info","kind":"function","ident_start":1720,"ident_end":1742,"extent_start":1716,"extent_end":2246,"fully_qualified_name":"get_unknown_board_info","ident_utf16":{"start":{"line_number":52,"utf16_col":4},"end":{"line_number":52,"utf16_col":26}},"extent_utf16":{"start":{"line_number":52,"utf16_col":0},"end":{"line_number":65,"utf16_col":34}}},{"name":"get_os_kernel_info","kind":"function","ident_start":2252,"ident_end":2270,"extent_start":2248,"extent_end":2351,"fully_qualified_name":"get_os_kernel_info","ident_utf16":{"start":{"line_number":67,"utf16_col":4},"end":{"line_number":67,"utf16_col":22}},"extent_utf16":{"start":{"line_number":67,"utf16_col":0},"end":{"line_number":69,"utf16_col":54}}},{"name":"get_ram_info","kind":"function","ident_start":2357,"ident_end":2369,"extent_start":2353,"extent_end":2715,"fully_qualified_name":"get_ram_info","ident_utf16":{"start":{"line_number":71,"utf16_col":4},"end":{"line_number":71,"utf16_col":16}},"extent_utf16":{"start":{"line_number":71,"utf16_col":0},"end":{"line_number":77,"utf16_col":25}}},{"name":"print_system_info","kind":"function","ident_start":2722,"ident_end":2739,"extent_start":2718,"extent_end":4189,"fully_qualified_name":"print_system_info","ident_utf16":{"start":{"line_number":80,"utf16_col":4},"end":{"line_number":80,"utf16_col":21}},"extent_utf16":{"start":{"line_number":80,"utf16_col":0},"end":{"line_number":118,"utf16_col":58}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"csrf_tokens":{"/Frix-x/klippain/branches":{"post":"dJTUoDFeNfWEwBXEcm7vgpzfXHCmUdD08yJOU_nDQiDGCeZj6begzjfMNIgdVSvpCXoeS3M91cUm53Ng7zHfjw"},"/repos/preferences":{"post":"hzBFiyWbHWri48ZN8qi-q6F84ca7rBqgjNAvMOP6FSQ0xDBNyIdlzocDxxfhbTwmeusAZ3I968uRUbT3YKSfBg"}}},"title":"klippain/scripts/system_info.py at main · Frix-x/klippain","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-83d4418b406d.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-bcc43f789400.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_streaming":true,"copilot_popover_file_editor_header":true,"copilot_smell_icebreaker_ux":false,"latest_commit_multi_author":true}}}</script>
  <div data-target="react-app.reactRoot"><style data-styled="true" data-styled-version="5.3.6">.fNPcqd{font-weight:600;font-size:32px;margin:0;font-size:14px;}/*!sc*/
.imcwCi{font-weight:600;font-size:32px;margin:0;font-size:16px;margin-left:8px;}/*!sc*/
.cgQnMS{font-weight:600;font-size:32px;margin:0;}/*!sc*/
.diwsLq{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:16px;}/*!sc*/
.jAEDJk{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:14px;}/*!sc*/
data-styled.g1[id="Heading__StyledHeading-sc-1c1dgg0-0"]{content:"fNPcqd,imcwCi,cgQnMS,diwsLq,jAEDJk,"}/*!sc*/
.fSWWem{padding:0;}/*!sc*/
.kPPmzM{max-width:100%;margin-left:auto;margin-right:auto;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;}/*!sc*/
.cIAPDV{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;}/*!sc*/
.gvCnwW{width:100%;}/*!sc*/
@media screen and (min-width:544px){.gvCnwW{width:100%;}}/*!sc*/
@media screen and (min-width:768px){.gvCnwW{width:auto;}}/*!sc*/
.kFEKvZ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-order:1;-ms-flex-order:1;order:1;width:100%;margin-left:0;margin-right:0;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin-bottom:0;min-width:0;}/*!sc*/
@media screen and (min-width:544px){.kFEKvZ{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}}/*!sc*/
@media screen and (min-width:768px){.kFEKvZ{width:auto;margin-top:0 !important;margin-bottom:0 !important;position:-webkit-sticky;position:sticky;top:0px;max-height:var(--sticky-pane-height);-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse;margin-right:0;}}/*!sc*/
@media screen and (min-width:769px){.kFEKvZ{height:100vh;max-height:100vh !important;}}/*!sc*/
@media print,screen and (max-width:1349px) and (min-width:768px){.kFEKvZ{display:none;}}/*!sc*/
.eUyHuk{margin-left:0;margin-right:0;display:none;margin-top:0;}/*!sc*/
@media screen and (min-width:768px){.eUyHuk{margin-left:0 !important;margin-right:0 !important;}}/*!sc*/
.hAeDYA{height:100%;position:relative;display:none;margin-left:0;}/*!sc*/
.dZCkhR{position:absolute;inset:0 -2px;cursor:col-resize;background-color:transparent;-webkit-transition-delay:0.1s;transition-delay:0.1s;}/*!sc*/
.dZCkhR:hover{background-color:rgba(110,118,129,0.4);}/*!sc*/
.gNdDUH{--pane-min-width:256px;--pane-max-width-diff:511px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));width:100%;padding:0;}/*!sc*/
@media screen and (min-width:544px){}/*!sc*/
@media screen and (min-width:768px){.gNdDUH{width:clamp(var(--pane-min-width),var(--pane-width),var(--pane-max-width));overflow:auto;}}/*!sc*/
@media screen and (min-width:1280px){.gNdDUH{--pane-max-width-diff:959px;}}/*!sc*/
.jywUSN{max-height:100%;height:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
@media screen and (max-width:768px){.jywUSN{display:none;}}/*!sc*/
@media screen and (min-width:768px){.jywUSN{max-height:100vh;height:100vh;}}/*!sc*/
.hBSSUC{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-left:16px;padding-right:16px;padding-bottom:8px;padding-top:16px;}/*!sc*/
.iPurHz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-bottom:16px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kkrdEu{-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}/*!sc*/
.trpoQ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;pointer-events:none;}/*!sc*/
.hVHHYa{margin-left:24px;margin-right:24px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.idZfsJ{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;}/*!sc*/
.bKgizp{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.bwTunw{margin-right:4px;color:#7d8590;}/*!sc*/
.caeYDk{font-size:14px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.jahcnb{margin-left:8px;white-space:nowrap;}/*!sc*/
.jahcnb:hover button:not(:hover){border-left-color:var(--button-default-borderColor-hover,var(--color-btn-hover-border));}/*!sc*/
.ccToMy{margin-left:16px;margin-right:16px;margin-bottom:12px;}/*!sc*/
@media screen and (max-width:768px){.ccToMy{display:none;}}/*!sc*/
.cNvKlH{margin-right:-6px;}/*!sc*/
.cLfAnm{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;max-height:100% !important;overflow-y:auto;-webkit-scrollbar-gutter:stable;-moz-scrollbar-gutter:stable;-ms-scrollbar-gutter:stable;scrollbar-gutter:stable;}/*!sc*/
@media screen and (max-width:768px){.cLfAnm{display:none;}}/*!sc*/
.erWCJP{padding-left:16px;padding-right:16px;padding-bottom:8px;}/*!sc*/
@media (min-height:600px) and (min-width:768px){.hwhShM{display:none;}}/*!sc*/
.cYPxpP{margin-top:8px;margin-left:16px;margin-right:16px;margin-bottom:12px;font-size:12px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
@media (max-height:599px),(max-width:767px){.fBtiVT{display:none;}}/*!sc*/
.emFMJu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-order:2;-ms-flex-order:2;order:2;-webkit-flex-basis:0;-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;min-width:1px;margin-right:auto;}/*!sc*/
@media print{.emFMJu{display:-webkit-box !important;display:-webkit-flex !important;display:-ms-flexbox !important;display:flex !important;}}/*!sc*/
.hlUAHL{width:100%;max-width:100%;margin-left:auto;margin-right:auto;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;padding:0;}/*!sc*/
.iStsmI{margin-left:auto;margin-right:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:40px;max-width:100%;margin-top:0;}/*!sc*/
.eIgvIk{display:inherit;}/*!sc*/
.eVFfWF{width:100%;}/*!sc*/
.kgXdnT{padding:16px;padding-bottom:0;}/*!sc*/
.kzTa-dF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:16px;width:100%;}/*!sc*/
.bbXCl{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;}/*!sc*/
.hGGMNu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;justify-self:flex-end;}/*!sc*/
.eHRrYV{margin-left:8px;margin-right:8px;}/*!sc*/
.dKmYfk{font-size:14px;min-width:0;max-width:125px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.hSNzKh{justify-self:end;max-width:100%;}/*!sc*/
.eTvGbF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:16px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kzRgrI{max-width:100%;}/*!sc*/
.cmAPIB{max-width:100%;list-style:none;display:inline-block;}/*!sc*/
.jwXCBK{display:inline-block;max-width:100%;}/*!sc*/
.bDwCYs{padding:16px;padding-bottom:0;padding-left:16px;padding-right:16px;}/*!sc*/
.fywjmm{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;}/*!sc*/
.dyczTK{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:8px;}/*!sc*/
.kszRgZ{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;padding-right:8px;min-width:0;}/*!sc*/
.gtBUEp{min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;}/*!sc*/
.MERGN{margin-left:16px;margin-right:16px;}/*!sc*/
@media screen and (min-width:1440px){.MERGN{margin-left:16px;}}/*!sc*/
.cMYnca{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
.brFBoI{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;border:1px solid;border-color:#30363d;border-radius:6px;margin-bottom:16px;}/*!sc*/
.eYedVD{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:273px;padding-right:8px;padding-left:16px;padding-top:8px;padding-bottom:8px;}/*!sc*/
.jGfYmh{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;}/*!sc*/
.lhFvfi{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bqgLjk{display:inherit;}/*!sc*/
@media screen and (min-width:544px){.bqgLjk{display:none;}}/*!sc*/
@media screen and (min-width:768px){.bqgLjk{display:none;}}/*!sc*/
.iJmJly{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}/*!sc*/
.kjydbF{width:100%;height:-webkit-fit-content;height:-moz-fit-content;height:fit-content;min-width:0;margin-right:16px;}/*!sc*/
.bSdwWB{padding-left:4px;padding-bottom:16px;}/*!sc*/
.fleZSW{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.fOEJrA{font-size:12px;-webkit-flex:auto;-ms-flex:auto;flex:auto;padding-right:16px;color:#7d8590;min-width:0;}/*!sc*/
.gBKNLX{top:0px;z-index:1;background:var(--color-canvas-default);position:-webkit-sticky;position:sticky;}/*!sc*/
.ePiodO{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;position:absolute;}/*!sc*/
.kQJlnf{display:none;min-width:0;padding-top:8px;padding-bottom:8px;}/*!sc*/
.gJICKO{margin-right:8px;margin-left:16px;text-overflow:ellipsis;overflow:hidden;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;width:100%;}/*!sc*/
.iZJewz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:14px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bESQXL{padding-left:8px;padding-top:8px;padding-bottom:8px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;background-color:#161b22;border:1px solid var(--borderColor-default,var(--color-border-default));border-radius:6px 6px 0px 0px;}/*!sc*/
.bfkNRF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:0;}/*!sc*/
.fXBLEV{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:transparent;}/*!sc*/
.fXBLEV:not(:last-child){margin-right:1px;}/*!sc*/
.fXBLEV:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.fXBLEV:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.fXBLEV:first-child{margin-left:-1px;}/*!sc*/
.fXBLEV:last-child{margin-right:-1px;}/*!sc*/
.gbKtit{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:#30363d;}/*!sc*/
.gbKtit:not(:last-child){margin-right:1px;}/*!sc*/
.gbKtit:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.gbKtit:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.gbKtit:first-child{margin-left:-1px;}/*!sc*/
.gbKtit:last-child{margin-right:-1px;}/*!sc*/
.iBylDf{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;margin-right:8px;}/*!sc*/
.kSGBPx{gap:8px;}/*!sc*/
.etfROT{border:1px solid;border-top:none;border-color:#30363d;border-radius:0px 0px 6px 6px;min-width:273px;}/*!sc*/
.jWnGGx{background-color:var(--bgColor-default,var(--color-canvas-default));border:0px;border-width:0;border-radius:0px 0px 6px 6px;padding:0;min-width:0;margin-top:46px;}/*!sc*/
.TCenl{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;padding-top:8px;padding-bottom:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;min-width:0;position:relative;}/*!sc*/
.cluMzC{position:relative;}/*!sc*/
.eRkHwF{-webkit-flex:1;-ms-flex:1;flex:1;position:relative;min-width:0;}/*!sc*/
.knCTAx{tab-size:8;isolation:isolate;position:relative;overflow:auto;max-width:unset;}/*!sc*/
.hXUKEK{margin:1px 8px;position:absolute;z-index:1;}/*!sc*/
.cXzIIR{position:absolute;}/*!sc*/
.ktQnIo{padding-bottom:33px;}/*!sc*/
.bgyiQy{background-color:#0d1117;border:1px solid;border-color:#30363d;border-radius:6px;contain:paint;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;height:100%;min-height:0;max-height:100vh;overflow-y:auto;right:0;top:0px;z-index:1;background:var(--color-canvas-default);position:-webkit-sticky;position:sticky;}/*!sc*/
.bJNAmt{padding-top:8px;padding-bottom:8px;padding-left:16px;padding-right:16px;}/*!sc*/
.ipXucK{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;}/*!sc*/
.wMEyi{font-size:14px;-webkit-order:1;-ms-flex-order:1;order:1;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-weight:600;}/*!sc*/
.OThit{font-size:12px;color:#7d8590;padding-top:8px;}/*!sc*/
.ckwgci{margin-right:6px;}/*!sc*/
.jGYebd{margin-left:-16px;margin-bottom:-8px;}/*!sc*/
.kgNotW{margin-bottom:-8px;overflow-y:auto;max-height:calc(100vh - 237px);padding-left:16px;padding-bottom:8px;padding-top:4px;}/*!sc*/
.cFPoqW{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}/*!sc*/
.brdoto{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;position:relative;margin-right:8px;}/*!sc*/
.kpISzB{background-color:#d2a8ff;opacity:0.1;position:absolute;border-radius:5px;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;height:100%;}/*!sc*/
.aiXQv{color:#d2a8ff;border-radius:5px;font-weight:600;font-size:smaller;padding-left:4px;padding-right:4px;padding-top:1px;padding-bottom:1px;}/*!sc*/
.aZrVR{position:fixed;top:0;right:0;height:100%;width:15px;-webkit-transition:-webkit-transform 0.3s;-webkit-transition:transform 0.3s;transition:transform 0.3s;z-index:1;}/*!sc*/
.aZrVR:hover{-webkit-transform:scaleX(1.5);-ms-transform:scaleX(1.5);transform:scaleX(1.5);}/*!sc*/
data-styled.g2[id="Box-sc-g0xbh4-0"]{content:"fSWWem,kPPmzM,cIAPDV,gvCnwW,kFEKvZ,eUyHuk,hAeDYA,dZCkhR,gNdDUH,jywUSN,hBSSUC,iPurHz,kkrdEu,trpoQ,hVHHYa,idZfsJ,bKgizp,bwTunw,caeYDk,jahcnb,ccToMy,cNvKlH,cLfAnm,erWCJP,hwhShM,cYPxpP,fBtiVT,emFMJu,hlUAHL,iStsmI,eIgvIk,eVFfWF,kgXdnT,kzTa-dF,bbXCl,hGGMNu,eHRrYV,dKmYfk,hSNzKh,eTvGbF,kzRgrI,cmAPIB,jwXCBK,bDwCYs,fywjmm,dyczTK,kszRgZ,gtBUEp,MERGN,cMYnca,brFBoI,eYedVD,jGfYmh,lhFvfi,bqgLjk,iJmJly,kjydbF,bSdwWB,fleZSW,fOEJrA,gBKNLX,ePiodO,kQJlnf,gJICKO,iZJewz,bESQXL,bfkNRF,fXBLEV,gbKtit,iBylDf,kSGBPx,etfROT,jWnGGx,TCenl,cluMzC,eRkHwF,knCTAx,hXUKEK,cXzIIR,ktQnIo,bgyiQy,bJNAmt,ipXucK,wMEyi,OThit,ckwgci,jGYebd,kgNotW,cFPoqW,brdoto,kpISzB,aiXQv,aZrVR,"}/*!sc*/
.rTZSs{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g3[id="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0"]{content:"rTZSs,"}/*!sc*/
.eKEtoB{display:inline-block;overflow:hidden;text-overflow:ellipsis;vertical-align:top;white-space:nowrap;max-width:125px;margin-left:4px;margin-right:8px;text-transform:capitalize;}/*!sc*/
.fUpWeN{display:inline-block;overflow:hidden;text-overflow:ellipsis;vertical-align:top;white-space:nowrap;max-width:125px;max-width:100%;}/*!sc*/
.iQHhGT{display:inherit;overflow:hidden;text-overflow:ellipsis;vertical-align:initial;white-space:nowrap;max-width:125px;max-width:180px;display:block;}/*!sc*/
data-styled.g5[id="Truncate__StyledTruncate-sc-23o1d2-0"]{content:"eKEtoB,fUpWeN,iQHhGT,"}/*!sc*/
.bJBoUI{color:#2f81f7;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bJBoUI:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.bJBoUI:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
.iJtJJh{color:#2f81f7;-webkit-text-decoration:none;text-decoration:none;font-weight:600;}/*!sc*/
.iJtJJh:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.iJtJJh:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
.hUWqlv{color:#2f81f7;-webkit-text-decoration:none;text-decoration:none;font-weight:400;}/*!sc*/
.hUWqlv:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.hUWqlv:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
data-styled.g7[id="Link__StyledLink-sc-14289xe-0"]{content:"bJBoUI,iJtJJh,hUWqlv,"}/*!sc*/
.hSXtjz{font-size:14px;line-height:20px;color:#e6edf3;vertical-align:middle;background-color:#0d1117;border:1px solid var(--control-borderColor-rest,#30363d);border-radius:6px;outline:none;box-shadow:0 0 transparent;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.hSXtjz input,.hSXtjz textarea{cursor:text;}/*!sc*/
.hSXtjz select{cursor:pointer;}/*!sc*/
.hSXtjz::-webkit-input-placeholder{color:#6e7681;}/*!sc*/
.hSXtjz::-moz-placeholder{color:#6e7681;}/*!sc*/
.hSXtjz:-ms-input-placeholder{color:#6e7681;}/*!sc*/
.hSXtjz::placeholder{color:#6e7681;}/*!sc*/
.hSXtjz:focus-within{border-color:#2f81f7;outline:none;box-shadow:inset 0 0 0 1px #2f81f7;}/*!sc*/
.hSXtjz > textarea{padding:12px;}/*!sc*/
@media (min-width:768px){.hSXtjz{font-size:14px;}}/*!sc*/
.fBrOQk{font-size:14px;line-height:20px;color:#e6edf3;vertical-align:middle;background-color:#0d1117;border:1px solid var(--control-borderColor-rest,#30363d);border-radius:6px;outline:none;box-shadow:0 0 transparent;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;min-height:32px;width:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-self:stretch;-ms-flex-item-align:stretch;align-self:stretch;margin-top:8px;border-radius:6px;}/*!sc*/
.fBrOQk input,.fBrOQk textarea{cursor:text;}/*!sc*/
.fBrOQk select{cursor:pointer;}/*!sc*/
.fBrOQk::-webkit-input-placeholder{color:#6e7681;}/*!sc*/
.fBrOQk::-moz-placeholder{color:#6e7681;}/*!sc*/
.fBrOQk:-ms-input-placeholder{color:#6e7681;}/*!sc*/
.fBrOQk::placeholder{color:#6e7681;}/*!sc*/
.fBrOQk > textarea{padding:12px;}/*!sc*/
@media (min-width:768px){.fBrOQk{font-size:14px;}}/*!sc*/
data-styled.g25[id="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0"]{content:"hSXtjz,fBrOQk,"}/*!sc*/
.hZMmEi{background-repeat:no-repeat;background-position:right 8px center;padding-left:12px;padding-right:12px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.hZMmEi > :not(:last-child){margin-right:8px;}/*!sc*/
.hZMmEi .TextInput-icon,.hZMmEi .TextInput-action{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;color:#7d8590;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;}/*!sc*/
.hZMmEi > input,.hZMmEi > select{padding-left:0;padding-right:0;}/*!sc*/
.jnWkuY{background-repeat:no-repeat;background-position:right 8px center;padding-left:12px;padding-right:0;margin-top:8px;border-radius:6px;}/*!sc*/
.jnWkuY > :not(:last-child){margin-right:8px;}/*!sc*/
.jnWkuY .TextInput-icon,.jnWkuY .TextInput-action{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;color:#7d8590;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;}/*!sc*/
.jnWkuY > input,.jnWkuY > select{padding-left:0;padding-right:0;}/*!sc*/
data-styled.g26[id="TextInputWrapper-sc-1mqhpbi-1"]{content:"hZMmEi,jnWkuY,"}/*!sc*/
.cmNjCr{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.cmNjCr:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.cmNjCr:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.cmNjCr:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.cmNjCr[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.cmNjCr[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cmNjCr:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.cmNjCr:active{-webkit-transition:none;transition:none;}/*!sc*/
.cmNjCr:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.cmNjCr:disabled [data-component=ButtonCounter],.cmNjCr:disabled [data-component="leadingVisual"],.cmNjCr:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.cmNjCr:focus{outline:solid 1px transparent;}}/*!sc*/
.cmNjCr [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cmNjCr[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.cmNjCr[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.cmNjCr[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.cmNjCr[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cmNjCr[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.cmNjCr[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.cmNjCr[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.cmNjCr[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cmNjCr[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.cmNjCr[data-block="block"]{width:100%;}/*!sc*/
.cmNjCr [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.cmNjCr [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.cmNjCr [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.cmNjCr [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.cmNjCr [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.cmNjCr [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cmNjCr:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.cmNjCr:active:not([disabled]){background-color:#161b22;}/*!sc*/
.cmNjCr[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.cmNjCr[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.cmNjCr[data-no-visuals]{color:#2f81f7;}/*!sc*/
.cmNjCr:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.cmNjCr:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.cmNjCr:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.cmNjCr{color:#7d8590;padding-left:8px;padding-right:8px;display:none;}/*!sc*/
@media screen and (max-width:768px){.cmNjCr{display:block;}}/*!sc*/
.lhczWi{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.lhczWi:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.lhczWi:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.lhczWi:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.lhczWi[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.lhczWi[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.lhczWi:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.lhczWi:active{-webkit-transition:none;transition:none;}/*!sc*/
.lhczWi:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.lhczWi:disabled [data-component=ButtonCounter],.lhczWi:disabled [data-component="leadingVisual"],.lhczWi:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.lhczWi:focus{outline:solid 1px transparent;}}/*!sc*/
.lhczWi [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.lhczWi[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.lhczWi[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.lhczWi[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.lhczWi[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.lhczWi[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.lhczWi[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.lhczWi[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.lhczWi[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.lhczWi[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.lhczWi[data-block="block"]{width:100%;}/*!sc*/
.lhczWi [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.lhczWi [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.lhczWi [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.lhczWi [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.lhczWi [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.lhczWi [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.lhczWi:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.lhczWi:active:not([disabled]){background-color:#161b22;}/*!sc*/
.lhczWi[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.lhczWi[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.lhczWi[data-no-visuals]{color:#2f81f7;}/*!sc*/
.lhczWi:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.lhczWi:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.lhczWi:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.lhczWi[data-no-visuals="true"]{color:#7d8590;height:32px;position:relative;}/*!sc*/
@media screen and (max-width:768px){.lhczWi[data-no-visuals="true"]{display:none;}}/*!sc*/
.hPfySA{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.hPfySA:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hPfySA:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hPfySA:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hPfySA[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hPfySA[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hPfySA:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hPfySA:active{-webkit-transition:none;transition:none;}/*!sc*/
.hPfySA:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.hPfySA:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hPfySA:focus{outline:solid 1px transparent;}}/*!sc*/
.hPfySA [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hPfySA[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hPfySA[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.hPfySA[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hPfySA[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hPfySA[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hPfySA[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hPfySA[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hPfySA[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hPfySA[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hPfySA[data-block="block"]{width:100%;}/*!sc*/
.hPfySA [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.hPfySA [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hPfySA [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hPfySA [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.hPfySA [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hPfySA [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hPfySA:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.hPfySA:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hPfySA[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hPfySA [data-component="leadingVisual"],.hPfySA [data-component="trailingVisual"],.hPfySA [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.hPfySA{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:0;}/*!sc*/
.hPfySA svg{color:#7d8590;}/*!sc*/
.hPfySA > span{width:inherit;}/*!sc*/
.dRdQkF{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.dRdQkF:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dRdQkF:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.dRdQkF:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dRdQkF[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.dRdQkF[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dRdQkF:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.dRdQkF:active{-webkit-transition:none;transition:none;}/*!sc*/
.dRdQkF:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.dRdQkF:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.dRdQkF:focus{outline:solid 1px transparent;}}/*!sc*/
.dRdQkF [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dRdQkF[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.dRdQkF[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.dRdQkF[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.dRdQkF[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dRdQkF[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.dRdQkF[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.dRdQkF[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.dRdQkF[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dRdQkF[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.dRdQkF[data-block="block"]{width:100%;}/*!sc*/
.dRdQkF [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.dRdQkF [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.dRdQkF [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.dRdQkF [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.dRdQkF [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.dRdQkF [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dRdQkF:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.dRdQkF:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.dRdQkF[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.dRdQkF [data-component="leadingVisual"],.dRdQkF [data-component="trailingVisual"],.dRdQkF [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.dRdQkF[data-no-visuals="true"]{color:#6e7681;border-top-right-radius:0;border-bottom-right-radius:0;border-right:0;}/*!sc*/
.dsmVIn{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.dsmVIn:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dsmVIn:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.dsmVIn:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dsmVIn[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.dsmVIn[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dsmVIn:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.dsmVIn:active{-webkit-transition:none;transition:none;}/*!sc*/
.dsmVIn:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.dsmVIn:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.dsmVIn:focus{outline:solid 1px transparent;}}/*!sc*/
.dsmVIn [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dsmVIn[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.dsmVIn[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.dsmVIn[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.dsmVIn[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dsmVIn[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.dsmVIn[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.dsmVIn[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.dsmVIn[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dsmVIn[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.dsmVIn[data-block="block"]{width:100%;}/*!sc*/
.dsmVIn [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.dsmVIn [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.dsmVIn [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.dsmVIn [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.dsmVIn [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.dsmVIn [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dsmVIn:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.dsmVIn:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.dsmVIn[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.dsmVIn [data-component="leadingVisual"],.dsmVIn [data-component="trailingVisual"],.dsmVIn [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.dsmVIn[data-no-visuals="true"]{color:#6e7681;font-size:14px;font-weight:400;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.ePclzw{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.ePclzw:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.ePclzw:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.ePclzw:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.ePclzw[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.ePclzw[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.ePclzw:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.ePclzw:active{-webkit-transition:none;transition:none;}/*!sc*/
.ePclzw:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.ePclzw:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.ePclzw:focus{outline:solid 1px transparent;}}/*!sc*/
.ePclzw [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ePclzw[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.ePclzw[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.ePclzw[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.ePclzw[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.ePclzw[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.ePclzw[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.ePclzw[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.ePclzw[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ePclzw[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.ePclzw[data-block="block"]{width:100%;}/*!sc*/
.ePclzw [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.ePclzw [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.ePclzw [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.ePclzw [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.ePclzw [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.ePclzw [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.ePclzw:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.ePclzw:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.ePclzw[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.ePclzw [data-component="leadingVisual"],.ePclzw [data-component="trailingVisual"],.ePclzw [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.ePclzw{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}/*!sc*/
.ePclzw svg{color:#7d8590;}/*!sc*/
.ePclzw > span{width:inherit;}/*!sc*/
.hPOZTU{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.hPOZTU:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hPOZTU:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hPOZTU:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hPOZTU[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hPOZTU[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hPOZTU:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hPOZTU:active{-webkit-transition:none;transition:none;}/*!sc*/
.hPOZTU:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.hPOZTU:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hPOZTU:focus{outline:solid 1px transparent;}}/*!sc*/
.hPOZTU [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hPOZTU[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hPOZTU[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.hPOZTU[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hPOZTU[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hPOZTU[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hPOZTU[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hPOZTU[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hPOZTU[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hPOZTU[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hPOZTU[data-block="block"]{width:100%;}/*!sc*/
.hPOZTU [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.hPOZTU [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hPOZTU [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hPOZTU [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.hPOZTU [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hPOZTU [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hPOZTU:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.hPOZTU:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hPOZTU[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hPOZTU [data-component="leadingVisual"],.hPOZTU [data-component="trailingVisual"],.hPOZTU [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.hPOZTU[data-no-visuals="true"]{border-top-left-radius:0;border-bottom-left-radius:0;display:none;}/*!sc*/
.jcILRt{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.jcILRt:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jcILRt:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jcILRt:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jcILRt[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jcILRt[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jcILRt:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jcILRt:active{-webkit-transition:none;transition:none;}/*!sc*/
.jcILRt:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.jcILRt:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jcILRt:focus{outline:solid 1px transparent;}}/*!sc*/
.jcILRt [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jcILRt[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jcILRt[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jcILRt[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jcILRt[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jcILRt[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jcILRt[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jcILRt[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jcILRt[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jcILRt[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jcILRt[data-block="block"]{width:100%;}/*!sc*/
.jcILRt [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.jcILRt [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jcILRt [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jcILRt [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.jcILRt [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jcILRt [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jcILRt:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.jcILRt:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.jcILRt[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.jcILRt [data-component="leadingVisual"],.jcILRt [data-component="trailingVisual"],.jcILRt [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.jcILRt[data-no-visuals="true"]{color:#7d8590;}/*!sc*/
.dzga-dt{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.dzga-dt:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dzga-dt:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.dzga-dt:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dzga-dt[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.dzga-dt[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dzga-dt:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.dzga-dt:active{-webkit-transition:none;transition:none;}/*!sc*/
.dzga-dt:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.dzga-dt:disabled [data-component=ButtonCounter],.dzga-dt:disabled [data-component="leadingVisual"],.dzga-dt:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.dzga-dt:focus{outline:solid 1px transparent;}}/*!sc*/
.dzga-dt [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dzga-dt[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.dzga-dt[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.dzga-dt[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.dzga-dt[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dzga-dt[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.dzga-dt[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.dzga-dt[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.dzga-dt[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dzga-dt[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.dzga-dt[data-block="block"]{width:100%;}/*!sc*/
.dzga-dt [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.dzga-dt [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.dzga-dt [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.dzga-dt [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.dzga-dt [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.dzga-dt [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dzga-dt:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.dzga-dt:active:not([disabled]){background-color:#161b22;}/*!sc*/
.dzga-dt[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.dzga-dt[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.dzga-dt[data-no-visuals]{color:#2f81f7;}/*!sc*/
.dzga-dt:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.dzga-dt:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.dzga-dt:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.dzga-dt[data-size="small"][data-no-visuals="true"]{margin-left:8px;}/*!sc*/
.dWukOn{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#e6edf3;background-color:transparent;box-shadow:none;}/*!sc*/
.dWukOn:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dWukOn:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.dWukOn:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.dWukOn[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.dWukOn[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dWukOn:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.dWukOn:active{-webkit-transition:none;transition:none;}/*!sc*/
.dWukOn:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.dWukOn:disabled [data-component=ButtonCounter],.dWukOn:disabled [data-component="leadingVisual"],.dWukOn:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.dWukOn:focus{outline:solid 1px transparent;}}/*!sc*/
.dWukOn [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dWukOn[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.dWukOn[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.dWukOn[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.dWukOn[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.dWukOn[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.dWukOn[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.dWukOn[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.dWukOn[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dWukOn[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.dWukOn[data-block="block"]{width:100%;}/*!sc*/
.dWukOn [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.dWukOn [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.dWukOn [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.dWukOn [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.dWukOn [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.dWukOn [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.dWukOn:hover:not([disabled]){background-color:#30363d;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dWukOn:active:not([disabled]){background-color:#161b22;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.dWukOn[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.dWukOn[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.dWukOn[data-no-visuals]{color:#2f81f7;}/*!sc*/
.dWukOn:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.dWukOn:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.dWukOn:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.dWukOn:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cuVVHm{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.cuVVHm:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.cuVVHm:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.cuVVHm:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.cuVVHm[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.cuVVHm[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cuVVHm:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.cuVVHm:active{-webkit-transition:none;transition:none;}/*!sc*/
.cuVVHm:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.cuVVHm:disabled [data-component=ButtonCounter],.cuVVHm:disabled [data-component="leadingVisual"],.cuVVHm:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.cuVVHm:focus{outline:solid 1px transparent;}}/*!sc*/
.cuVVHm [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cuVVHm[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.cuVVHm[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;color:#e6edf3;display:none;}/*!sc*/
.cuVVHm[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.cuVVHm[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cuVVHm[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.cuVVHm[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
@media screen and (min-width:544px){.cuVVHm[data-size="small"]{display:none;}}/*!sc*/
@media screen and (min-width:768px){.cuVVHm[data-size="small"]{display:block;}}/*!sc*/
@media screen and (min-width:1012px){.cuVVHm[data-size="small"]{display:block;}}/*!sc*/
.cuVVHm[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.cuVVHm[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cuVVHm[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.cuVVHm[data-block="block"]{width:100%;}/*!sc*/
.cuVVHm [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.cuVVHm [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.cuVVHm [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.cuVVHm [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.cuVVHm [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.cuVVHm [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cuVVHm:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.cuVVHm:active:not([disabled]){background-color:#161b22;}/*!sc*/
.cuVVHm[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.cuVVHm[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.cuVVHm[data-no-visuals]{color:#2f81f7;}/*!sc*/
.cuVVHm:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.cuVVHm:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.cuVVHm:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.kGDoCG{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.kGDoCG:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.kGDoCG:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.kGDoCG:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.kGDoCG[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.kGDoCG[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.kGDoCG:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.kGDoCG:active{-webkit-transition:none;transition:none;}/*!sc*/
.kGDoCG:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.kGDoCG:disabled [data-component=ButtonCounter],.kGDoCG:disabled [data-component="leadingVisual"],.kGDoCG:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.kGDoCG:focus{outline:solid 1px transparent;}}/*!sc*/
.kGDoCG [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.kGDoCG[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.kGDoCG[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;color:#e6edf3;margin-left:8px;}/*!sc*/
.kGDoCG[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.kGDoCG[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.kGDoCG[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.kGDoCG[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.kGDoCG[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.kGDoCG[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.kGDoCG[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.kGDoCG[data-block="block"]{width:100%;}/*!sc*/
.kGDoCG [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.kGDoCG [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.kGDoCG [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.kGDoCG [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.kGDoCG [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.kGDoCG [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.kGDoCG:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.kGDoCG:active:not([disabled]){background-color:#161b22;}/*!sc*/
.kGDoCG[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.kGDoCG[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.kGDoCG[data-no-visuals]{color:#2f81f7;}/*!sc*/
.kGDoCG:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.kGDoCG:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.kGDoCG:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.hHvcfT{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;padding-left:8px;padding-right:8px;}/*!sc*/
.hHvcfT:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hHvcfT:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hHvcfT:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.hHvcfT[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hHvcfT[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hHvcfT:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hHvcfT:active{-webkit-transition:none;transition:none;}/*!sc*/
.hHvcfT:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.hHvcfT:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hHvcfT:focus{outline:solid 1px transparent;}}/*!sc*/
.hHvcfT [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hHvcfT[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hHvcfT[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.hHvcfT[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hHvcfT[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hHvcfT[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hHvcfT[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hHvcfT[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hHvcfT[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hHvcfT[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hHvcfT[data-block="block"]{width:100%;}/*!sc*/
.hHvcfT [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.hHvcfT [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hHvcfT [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hHvcfT [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.hHvcfT [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hHvcfT [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hHvcfT:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.hHvcfT:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hHvcfT[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.hHvcfT [data-component="leadingVisual"],.hHvcfT [data-component="trailingVisual"],.hHvcfT [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.hHvcfT linkButtonSx:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hHvcfT linkButtonSx:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hHvcfT linkButtonSx:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.kCdBku{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.kCdBku:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.kCdBku:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.kCdBku:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.kCdBku[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.kCdBku[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.kCdBku:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.kCdBku:active{-webkit-transition:none;transition:none;}/*!sc*/
.kCdBku:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.kCdBku:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.kCdBku:focus{outline:solid 1px transparent;}}/*!sc*/
.kCdBku [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.kCdBku[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.kCdBku[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.kCdBku[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.kCdBku[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.kCdBku[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.kCdBku[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.kCdBku[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.kCdBku[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.kCdBku[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.kCdBku[data-block="block"]{width:100%;}/*!sc*/
.kCdBku [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.kCdBku [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.kCdBku [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.kCdBku [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.kCdBku [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.kCdBku [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.kCdBku:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.kCdBku:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.kCdBku[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.kCdBku [data-component="leadingVisual"],.kCdBku [data-component="trailingVisual"],.kCdBku [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.jcdBXR{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.jcdBXR:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jcdBXR:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jcdBXR:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jcdBXR[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jcdBXR[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jcdBXR:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jcdBXR:active{-webkit-transition:none;transition:none;}/*!sc*/
.jcdBXR:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.jcdBXR:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jcdBXR:focus{outline:solid 1px transparent;}}/*!sc*/
.jcdBXR [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jcdBXR[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jcdBXR[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jcdBXR[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jcdBXR[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jcdBXR[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jcdBXR[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jcdBXR[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jcdBXR[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jcdBXR[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jcdBXR[data-block="block"]{width:100%;}/*!sc*/
.jcdBXR [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.jcdBXR [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jcdBXR [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jcdBXR [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.jcdBXR [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jcdBXR [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jcdBXR:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.jcdBXR:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.jcdBXR[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.jcdBXR [data-component="leadingVisual"],.jcdBXR [data-component="trailingVisual"],.jcdBXR [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.jcdBXR[data-size="small"][data-no-visuals="true"]{border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.bpoOwX{border-radius:6px;border:1px solid;border-color:rgba(240,246,252,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#c9d1d9;background-color:#21262d;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.bpoOwX:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.bpoOwX:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bpoOwX:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.bpoOwX[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bpoOwX[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bpoOwX:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bpoOwX:active{-webkit-transition:none;transition:none;}/*!sc*/
.bpoOwX:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.bpoOwX:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bpoOwX:focus{outline:solid 1px transparent;}}/*!sc*/
.bpoOwX [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bpoOwX[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bpoOwX[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bpoOwX[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bpoOwX[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bpoOwX[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bpoOwX[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bpoOwX[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bpoOwX[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bpoOwX[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bpoOwX[data-block="block"]{width:100%;}/*!sc*/
.bpoOwX [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.bpoOwX [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bpoOwX [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bpoOwX [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.bpoOwX [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bpoOwX [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bpoOwX:hover:not([disabled]){background-color:#30363d;border-color:#8b949e;}/*!sc*/
.bpoOwX:active:not([disabled]){background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.bpoOwX[aria-expanded=true]{background-color:hsla(212,12%,18%,1);border-color:#6e7681;}/*!sc*/
.bpoOwX [data-component="leadingVisual"],.bpoOwX [data-component="trailingVisual"],.bpoOwX [data-component="trailingAction"]{color:#7d8590;}/*!sc*/
.bpoOwX[data-size="small"][data-no-visuals="true"]{border-top-right-radius:0;border-bottom-right-radius:0;border-right-width:0;}/*!sc*/
.bpoOwX[data-size="small"][data-no-visuals="true"]:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bpoOwX[data-size="small"][data-no-visuals="true"]:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bpoOwX[data-size="small"][data-no-visuals="true"]:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bhUFcA{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.bhUFcA:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.bhUFcA:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bhUFcA:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.bhUFcA[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bhUFcA[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bhUFcA:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bhUFcA:active{-webkit-transition:none;transition:none;}/*!sc*/
.bhUFcA:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.bhUFcA:disabled [data-component=ButtonCounter],.bhUFcA:disabled [data-component="leadingVisual"],.bhUFcA:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bhUFcA:focus{outline:solid 1px transparent;}}/*!sc*/
.bhUFcA [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bhUFcA[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bhUFcA[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bhUFcA[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bhUFcA[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bhUFcA[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bhUFcA[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bhUFcA[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bhUFcA[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bhUFcA[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bhUFcA[data-block="block"]{width:100%;}/*!sc*/
.bhUFcA [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.bhUFcA [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bhUFcA [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bhUFcA [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.bhUFcA [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bhUFcA [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bhUFcA:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.bhUFcA:active:not([disabled]){background-color:#161b22;}/*!sc*/
.bhUFcA[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.bhUFcA[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.bhUFcA[data-no-visuals]{color:#2f81f7;}/*!sc*/
.bhUFcA:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.bhUFcA:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.bhUFcA:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.bhUFcA[data-size="small"][data-no-visuals="true"]{color:#7d8590;position:relative;}/*!sc*/
.jYfgHQ{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.jYfgHQ:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jYfgHQ:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jYfgHQ:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.jYfgHQ[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jYfgHQ[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jYfgHQ:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jYfgHQ:active{-webkit-transition:none;transition:none;}/*!sc*/
.jYfgHQ:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.jYfgHQ:disabled [data-component=ButtonCounter],.jYfgHQ:disabled [data-component="leadingVisual"],.jYfgHQ:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jYfgHQ:focus{outline:solid 1px transparent;}}/*!sc*/
.jYfgHQ [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jYfgHQ[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jYfgHQ[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jYfgHQ[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jYfgHQ[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jYfgHQ[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jYfgHQ[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jYfgHQ[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jYfgHQ[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jYfgHQ[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jYfgHQ[data-block="block"]{width:100%;}/*!sc*/
.jYfgHQ [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.jYfgHQ [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jYfgHQ [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jYfgHQ [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.jYfgHQ [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jYfgHQ [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jYfgHQ:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.jYfgHQ:active:not([disabled]){background-color:#161b22;}/*!sc*/
.jYfgHQ[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.jYfgHQ[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.jYfgHQ[data-no-visuals]{color:#2f81f7;}/*!sc*/
.jYfgHQ:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.jYfgHQ:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.jYfgHQ:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.jYfgHQ[data-size="small"][data-no-visuals="true"]{color:#7d8590;}/*!sc*/
.iGBjJv{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#2f81f7;background-color:transparent;box-shadow:none;}/*!sc*/
.iGBjJv:focus:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.iGBjJv:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iGBjJv:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #2f81f7;outline-offset:-2px;}/*!sc*/
.iGBjJv[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iGBjJv[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iGBjJv:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iGBjJv:active{-webkit-transition:none;transition:none;}/*!sc*/
.iGBjJv:disabled{cursor:not-allowed;box-shadow:none;color:#484f58;}/*!sc*/
.iGBjJv:disabled [data-component=ButtonCounter],.iGBjJv:disabled [data-component="leadingVisual"],.iGBjJv:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iGBjJv:focus{outline:solid 1px transparent;}}/*!sc*/
.iGBjJv [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iGBjJv[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iGBjJv[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iGBjJv[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iGBjJv[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iGBjJv[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iGBjJv[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iGBjJv[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iGBjJv[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iGBjJv[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iGBjJv[data-block="block"]{width:100%;}/*!sc*/
.iGBjJv [data-component="leadingVisual"]{grid-area:leadingVisual;color:#7d8590;}/*!sc*/
.iGBjJv [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iGBjJv [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iGBjJv [data-component="trailingAction"]{margin-right:-4px;color:#7d8590;}/*!sc*/
.iGBjJv [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iGBjJv [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iGBjJv:hover:not([disabled]){background-color:#30363d;}/*!sc*/
.iGBjJv:active:not([disabled]){background-color:#161b22;}/*!sc*/
.iGBjJv[aria-expanded=true]{background-color:#161b22;}/*!sc*/
.iGBjJv[data-component="IconButton"][data-no-visuals]{color:#7d8590;}/*!sc*/
.iGBjJv[data-no-visuals]{color:#2f81f7;}/*!sc*/
.iGBjJv:has([data-component="ButtonCounter"]){color:#2f81f7;}/*!sc*/
.iGBjJv:disabled[data-no-visuals]{color:#484f58;}/*!sc*/
.iGBjJv:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.iGBjJv[data-no-visuals="true"]{-webkit-order:3;-ms-flex-order:3;order:3;color:#e6edf3;margin-right:-8px;}/*!sc*/
data-styled.g27[id="types__StyledButton-sc-ws60qy-0"]{content:"cmNjCr,lhczWi,hPfySA,dRdQkF,dsmVIn,ePclzw,hPOZTU,jcILRt,dzga-dt,dWukOn,cuVVHm,kGDoCG,hHvcfT,kCdBku,jcdBXR,bpoOwX,bhUFcA,jYfgHQ,iGBjJv,"}/*!sc*/
.fCnxTL{position:relative;display:inline-block;}/*!sc*/
.fCnxTL::before{position:absolute;z-index:1000001;display:none;width:0px;height:0px;color:#6e7681;pointer-events:none;content:'';border:6px solid transparent;opacity:0;}/*!sc*/
.fCnxTL::after{position:absolute;z-index:1000000;display:none;padding:0.5em 0.75em;font:normal normal 11px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";-webkit-font-smoothing:subpixel-antialiased;color:#ffffff;text-align:center;-webkit-text-decoration:none;text-decoration:none;text-shadow:none;text-transform:none;-webkit-letter-spacing:normal;-moz-letter-spacing:normal;-ms-letter-spacing:normal;letter-spacing:normal;word-wrap:break-word;white-space:pre;pointer-events:none;content:attr(aria-label);background:#6e7681;border-radius:3px;opacity:0;}/*!sc*/
@-webkit-keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
@keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
.fCnxTL:hover::before,.fCnxTL:active::before,.fCnxTL:focus::before,.fCnxTL:focus-within::before,.fCnxTL:hover::after,.fCnxTL:active::after,.fCnxTL:focus::after,.fCnxTL:focus-within::after{display:inline-block;-webkit-text-decoration:none;text-decoration:none;-webkit-animation-name:tooltip-appear;animation-name:tooltip-appear;-webkit-animation-duration:0.1s;animation-duration:0.1s;-webkit-animation-fill-mode:forwards;animation-fill-mode:forwards;-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-animation-delay:0.4s;animation-delay:0.4s;}/*!sc*/
.fCnxTL.tooltipped-no-delay:hover::before,.fCnxTL.tooltipped-no-delay:active::before,.fCnxTL.tooltipped-no-delay:focus::before,.fCnxTL.tooltipped-no-delay:focus-within::before,.fCnxTL.tooltipped-no-delay:hover::after,.fCnxTL.tooltipped-no-delay:active::after,.fCnxTL.tooltipped-no-delay:focus::after,.fCnxTL.tooltipped-no-delay:focus-within::after{-webkit-animation-delay:0s;animation-delay:0s;}/*!sc*/
.fCnxTL.tooltipped-multiline:hover::after,.fCnxTL.tooltipped-multiline:active::after,.fCnxTL.tooltipped-multiline:focus::after,.fCnxTL.tooltipped-multiline:focus-within::after{display:table-cell;}/*!sc*/
.fCnxTL.tooltipped-s::after,.fCnxTL.tooltipped-se::after,.fCnxTL.tooltipped-sw::after{top:100%;right:50%;margin-top:6px;}/*!sc*/
.fCnxTL.tooltipped-s::before,.fCnxTL.tooltipped-se::before,.fCnxTL.tooltipped-sw::before{top:auto;right:50%;bottom:-7px;margin-right:-6px;border-bottom-color:#6e7681;}/*!sc*/
.fCnxTL.tooltipped-se::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.fCnxTL.tooltipped-sw::after{margin-right:-16px;}/*!sc*/
.fCnxTL.tooltipped-n::after,.fCnxTL.tooltipped-ne::after,.fCnxTL.tooltipped-nw::after{right:50%;bottom:100%;margin-bottom:6px;}/*!sc*/
.fCnxTL.tooltipped-n::before,.fCnxTL.tooltipped-ne::before,.fCnxTL.tooltipped-nw::before{top:-7px;right:50%;bottom:auto;margin-right:-6px;border-top-color:#6e7681;}/*!sc*/
.fCnxTL.tooltipped-ne::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.fCnxTL.tooltipped-nw::after{margin-right:-16px;}/*!sc*/
.fCnxTL.tooltipped-s::after,.fCnxTL.tooltipped-n::after{-webkit-transform:translateX(50%);-ms-transform:translateX(50%);transform:translateX(50%);}/*!sc*/
.fCnxTL.tooltipped-w::after{right:100%;bottom:50%;margin-right:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.fCnxTL.tooltipped-w::before{top:50%;bottom:50%;left:-7px;margin-top:-6px;border-left-color:#6e7681;}/*!sc*/
.fCnxTL.tooltipped-e::after{bottom:50%;left:100%;margin-left:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.fCnxTL.tooltipped-e::before{top:50%;right:-7px;bottom:50%;margin-top:-6px;border-right-color:#6e7681;}/*!sc*/
.fCnxTL.tooltipped-multiline::after{width:-webkit-max-content;width:-moz-max-content;width:max-content;max-width:250px;word-wrap:break-word;white-space:pre-line;border-collapse:separate;}/*!sc*/
.fCnxTL.tooltipped-multiline.tooltipped-s::after,.fCnxTL.tooltipped-multiline.tooltipped-n::after{right:auto;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);}/*!sc*/
.fCnxTL.tooltipped-multiline.tooltipped-w::after,.fCnxTL.tooltipped-multiline.tooltipped-e::after{right:100%;}/*!sc*/
.fCnxTL.tooltipped-align-right-2::after{right:0;margin-right:0;}/*!sc*/
.fCnxTL.tooltipped-align-right-2::before{right:15px;}/*!sc*/
.fCnxTL.tooltipped-align-left-2::after{left:0;margin-left:0;}/*!sc*/
.fCnxTL.tooltipped-align-left-2::before{left:10px;}/*!sc*/
data-styled.g28[id="Tooltip__TooltipBase-sc-uha8qm-0"]{content:"fCnxTL,"}/*!sc*/
.cDLBls{border:0;font-size:inherit;font-family:inherit;background-color:transparent;-webkit-appearance:none;color:inherit;width:100%;}/*!sc*/
.cDLBls:focus{outline:0;}/*!sc*/
data-styled.g29[id="UnstyledTextInput-sc-14ypya-0"]{content:"cDLBls,"}/*!sc*/
.bOMzPg{min-width:0;}/*!sc*/
.fWVgeN{padding-left:4px;padding-right:4px;font-weight:400;color:#7d8590;font-size:16px;}/*!sc*/
.hfRvxg{color:#e6edf3;}/*!sc*/
.kfsdZq{color:#7d8590;margin-right:4px;}/*!sc*/
.iqTHmv{padding-left:4px;padding-right:4px;font-weight:400;color:#7d8590;font-size:14px;}/*!sc*/
data-styled.g35[id="Text-sc-17v1xeu-0"]{content:"bOMzPg,fWVgeN,hfRvxg,gPDEWA,kfsdZq,iqTHmv,"}/*!sc*/
.cjbBGq{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle;isolation:isolate;}/*!sc*/
.cjbBGq.cjbBGq > *{margin-inline-end:-1px;position:relative;border-radius:0;}/*!sc*/
.cjbBGq.cjbBGq > *:first-child{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:last-child{border-top-right-radius:6px;border-bottom-right-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:focus,.cjbBGq.cjbBGq > *:active,.cjbBGq.cjbBGq > *:hover{z-index:1;}/*!sc*/
data-styled.g84[id="ButtonGroup-sc-1gxhls1-0"]{content:"cjbBGq,"}/*!sc*/
.bFrOJy{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:600;padding:0;height:100%;width:100%;}/*!sc*/
.bFrOJy .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:#0d1117;border-color:#6e7681;border-style:solid;border-width:1px;border-radius:var(--segmented-control-outer-radius);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:var(--segmented-control-button-inner-padding);padding-right:var(--segmented-control-button-inner-padding);}/*!sc*/
.bFrOJy svg{fill:#7d8590;}/*!sc*/
.bFrOJy:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.bFrOJy .segmentedControl-text:after{content:"Code";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.bFrOJy:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
.dAXkSP{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:400;padding:var(--segmented-control-button-bg-inset);height:100%;width:100%;}/*!sc*/
.dAXkSP .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:transparent;border-color:transparent;border-style:solid;border-width:1px;border-radius:calc(var(--segmented-control-outer-radius) - var(--segmented-control-button-bg-inset) / 2);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));padding-right:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));}/*!sc*/
.dAXkSP svg{fill:#7d8590;}/*!sc*/
.dAXkSP:hover .segmentedControl-content{background-color:#30363d;}/*!sc*/
.dAXkSP:active .segmentedControl-content{background-color:#21262d;}/*!sc*/
.dAXkSP:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.dAXkSP .segmentedControl-text:after{content:"Blame";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.dAXkSP:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
data-styled.g91[id="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0"]{content:"bFrOJy,dAXkSP,"}/*!sc*/
.ivYJSK{background-color:rgba(110,118,129,0.1);border-radius:6px;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;font-size:14px;height:28px;margin:0;padding:0;}/*!sc*/
data-styled.g93[id="SegmentedControl__SegmentedControlList-sc-1rzig82-0"]{content:"ivYJSK,"}/*!sc*/
body[data-page-layout-dragging="true"]{cursor:col-resize;}/*!sc*/
body[data-page-layout-dragging="true"] *{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}/*!sc*/
data-styled.g97[id="sc-global-gbKrvU1"]{content:"sc-global-gbKrvU1,"}/*!sc*/
.hLwWNO{list-style:none;padding:0;margin:0;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item{outline:none;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item:focus-visible > div,.hLwWNO .PRIVATE_TreeView-item.focus-visible > div{box-shadow:inset 0 0 0 2px #2f81f7;}/*!sc*/
@media (forced-colors:active){.hLwWNO .PRIVATE_TreeView-item:focus-visible > div,.hLwWNO .PRIVATE_TreeView-item.focus-visible > div{outline:2px solid HighlightText;outline-offset:-2;}}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-container{--level:1;--toggle-width:1rem;position:relative;display:grid;grid-template-columns:calc(calc(var(--level) - 1) * (var(--toggle-width) / 2)) var(--toggle-width) 1fr;grid-template-areas:'spacer toggle content';width:100%;min-height:2rem;font-size:14px;color:#e6edf3;border-radius:6px;cursor:pointer;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-container:hover{background-color:rgba(177,186,196,0.12);}/*!sc*/
@media (forced-colors:active){.hLwWNO .PRIVATE_TreeView-item-container:hover{outline:2px solid transparent;outline-offset:-2px;}}/*!sc*/
@media (pointer:coarse){.hLwWNO .PRIVATE_TreeView-item-container{--toggle-width:1.5rem;min-height:2.75rem;}}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{background-color:transparent;cursor:default;}/*!sc*/
@media (forced-colors:active){.hLwWNO .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{outline:none;}}/*!sc*/
.hLwWNO[data-omit-spacer='true'] .PRIVATE_TreeView-item-container{grid-template-columns:0 0 1fr;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container{background-color:rgba(177,186,196,0.08);}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{content:'';position:absolute;top:calc(50% - 0.75rem);left:-8px;width:0.25rem;height:1.5rem;background-color:#2f81f7;border-radius:6px;}/*!sc*/
@media (forced-colors:active){.hLwWNO .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{background-color:HighlightText;}}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-toggle{grid-area:toggle;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;height:100%;color:#7d8590;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-toggle--hover:hover{background-color:rgba(177,186,196,0.12);}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-toggle--end{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-content{grid-area:content;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:100%;padding:0 8px;gap:8px;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-content-text{-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-visual{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;color:#7d8590;}/*!sc*/
.hLwWNO .PRIVATE_TreeView-item-level-line{width:100%;height:100%;border-right:1px solid;border-color:rgba(240,246,252,0.1);}/*!sc*/
@media (hover:hover){.hLwWNO .PRIVATE_TreeView-item-level-line{border-color:transparent;}.hLwWNO:hover .PRIVATE_TreeView-item-level-line,.hLwWNO:focus-within .PRIVATE_TreeView-item-level-line{border-color:rgba(240,246,252,0.1);}}/*!sc*/
.hLwWNO .PRIVATE_TreeView-directory-icon{display:grid;color:#7d8590;}/*!sc*/
.hLwWNO .PRIVATE_VisuallyHidden{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g104[id="TreeView__UlBox-sc-4ex6b6-0"]{content:"hLwWNO,"}/*!sc*/
</style><meta data-hydrostats="publish"/> <!-- --> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-g0xbh4-0"><div style="--sticky-pane-height:100vh" class="Box-sc-g0xbh4-0 fSWWem"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 kFEKvZ"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div class="Box-sc-g0xbh4-0 hAeDYA"><div role="separator" class="Box-sc-g0xbh4-0 dZCkhR"></div></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 gNdDUH"><span class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"><form><label for=":Rdjal5:-width-input">Pane width</label><p id=":Rdjal5:-input-hint">Use a value between <!-- -->0<!-- -->% and <!-- -->0<!-- -->%</p><input id=":Rdjal5:-width-input" aria-describedby=":Rdjal5:-input-hint" name="pane-width" inputMode="numeric" pattern="[0-9]*" autoCorrect="off" autoComplete="off" type="text" value=""/><button type="submit">Change width</button></form></span><div class="Box-sc-g0xbh4-0 react-tree-pane-contents-3-panel"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jywUSN"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 cmNjCr"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 lhczWi" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 hPfySA react-repos-tree-pane-ref-selector width-full ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 bwTunw"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dRdQkF" href="/Frix-x/klippain/new/main/scripts"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dsmVIn"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="Box-sc-g0xbh4-0 ccToMy"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 hSXtjz hZMmEi TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autoCorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""/><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 cLfAnm"><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 hLwWNO"><li class="PRIVATE_TreeView-item" tabindex="0" id=".github-item" role="treeitem" aria-labelledby=":Rqcndjal5:" aria-describedby=":Rqcndjal5H1: :Rqcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>.github</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="adxl_results-item" role="treeitem" aria-labelledby=":R1acndjal5:" aria-describedby=":R1acndjal5H1: :R1acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R1acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>adxl_results</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="config-item" role="treeitem" aria-labelledby=":R1qcndjal5:" aria-describedby=":R1qcndjal5H1: :R1qcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R1qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>config</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="docs-item" role="treeitem" aria-labelledby=":R2acndjal5:" aria-describedby=":R2acndjal5H1: :R2acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R2acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>docs</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="macros-item" role="treeitem" aria-labelledby=":R2qcndjal5:" aria-describedby=":R2qcndjal5H1: :R2qcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R2qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>macros</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="moonraker-item" role="treeitem" aria-labelledby=":R3acndjal5:" aria-describedby=":R3acndjal5H1: :R3acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R3acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>moonraker</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts-item" role="treeitem" aria-labelledby=":R3qcndjal5:" aria-describedby=":R3qcndjal5H1: :R3qcndjal5H2:" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R3qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>scripts</span></span></div></div><ul role="group" style="list-style:none;padding:0;margin:0"><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts/gcode_shell_command.py-item" role="treeitem" aria-labelledby=":Rbbqcndjal5:" aria-describedby=":Rbbqcndjal5H1: :Rbbqcndjal5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rbbqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rbbqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>gcode_shell_command.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts/graph_vibrations.py-item" role="treeitem" aria-labelledby=":Rjbqcndjal5:" aria-describedby=":Rjbqcndjal5H1: :Rjbqcndjal5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rjbqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rjbqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>graph_vibrations.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts/plot_graphs.sh-item" role="treeitem" aria-labelledby=":Rrbqcndjal5:" aria-describedby=":Rrbqcndjal5H1: :Rrbqcndjal5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rrbqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rrbqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>plot_graphs.sh</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts/shell_commands.cfg-item" role="treeitem" aria-labelledby=":R13bqcndjal5:" aria-describedby=":R13bqcndjal5H1: :R13bqcndjal5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R13bqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R13bqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>shell_commands.cfg</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="scripts/system_info.py-item" role="treeitem" aria-labelledby=":R1bbqcndjal5:" aria-describedby=":R1bbqcndjal5H1: :R1bbqcndjal5H2:" aria-level="2" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R1bbqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1bbqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>system_info.py</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item" tabindex="0" id="user_templates-item" role="treeitem" aria-labelledby=":R4acndjal5:" aria-describedby=":R4acndjal5H1: :R4acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R4acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>user_templates</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".gitignore-item" role="treeitem" aria-labelledby=":R4qcndjal5:" aria-describedby=":R4qcndjal5H1: :R4qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="LICENSE-item" role="treeitem" aria-labelledby=":R5acndjal5:" aria-describedby=":R5acndjal5H1: :R5acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>LICENSE</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="README.md-item" role="treeitem" aria-labelledby=":R5qcndjal5:" aria-describedby=":R5qcndjal5H1: :R5qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="install.sh-item" role="treeitem" aria-labelledby=":R6acndjal5:" aria-describedby=":R6acndjal5H1: :R6acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R6acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>install.sh</span></span></div></div></li></ul></nav></div></div><div class="Box-sc-g0xbh4-0 hwhShM"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Share feedback</a></div></div></div><div class="Box-sc-g0xbh4-0 fBtiVT"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Share feedback</a></div></div></div></div></div></div></div><main class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="Box-sc-g0xbh4-0 kgXdnT react-code-view-header--narrow"><div class="Box-sc-g0xbh4-0 kzTa-dF"><div class="Box-sc-g0xbh4-0 bbXCl"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 cmNjCr"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 lhczWi" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><div class="Box-sc-g0xbh4-0 hGGMNu"><div class="Box-sc-g0xbh4-0 eHRrYV"><button type="button" id="branch-picker-repos-header-ref-selector-narrow" aria-haspopup="true" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 ePclzw ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 bwTunw"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dKmYfk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hPOZTU"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 jcILRt js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9aaqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div><div class="Box-sc-g0xbh4-0 hSNzKh"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-mobile-heading" id="repos-header-breadcrumb-mobile" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-mobile-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 iJtJJh" href="/Frix-x/klippain/tree/main">klippain</a></li><li class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><a sx="[object Object]" class="Link__StyledLink-sc-14289xe-0 hUWqlv" href="/Frix-x/klippain/tree/main/scripts">scripts</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><h1 tabindex="-1" id="file-name-id-mobile" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">system_info.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dzga-dt"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div></div><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs react-code-view-header--wide"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-wide-heading" id="repos-header-breadcrumb-wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 iJtJJh" href="/Frix-x/klippain/tree/main">klippain</a></li><li class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><a sx="[object Object]" class="Link__StyledLink-sc-14289xe-0 hUWqlv" href="/Frix-x/klippain/tree/main/scripts">scripts</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">system_info.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dzga-dt"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hPOZTU"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 jcILRt js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9pkqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MERGN react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div><div class="Box-sc-g0xbh4-0"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 MERGN"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-g0xbh4-0 brFBoI"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="Box-sc-g0xbh4-0 jGfYmh"><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"></div><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 dWukOn react-last-commit-history-group" href="/Frix-x/klippain/commits/main/scripts/system_info.py" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 hfRvxg">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"></div><span role="tooltip" aria-label="Commit history" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-n"><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 dWukOn react-last-commit-history-icon" href="/Frix-x/klippain/commits/main/scripts/system_info.py"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 kjydbF container"><div class="Box-sc-g0xbh4-0 bSdwWB react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fOEJrA text-mono"><div title="executable file" class="Truncate__StyledTruncate-sc-23o1d2-0 eKEtoB"><span class="Text-sc-17v1xeu-0 gPDEWA">executable file</span></div><span class="Text-sc-17v1xeu-0 kfsdZq">·</span><div title="4.14 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">123 lines (97 loc) · 4.14 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-banner"><button type="button" id=":R2bqlajal5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 cuVVHm"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6.25 9a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 6.25 9Zm4.25.75a.75.75 0 0 0-1.5 0v1.5a.75.75 0 0 0 1.5 0v-1.5Z"></path><path d="M7.86 1.77c.05.053.097.107.14.164.043-.057.09-.111.14-.164.681-.731 1.737-.9 2.943-.765 1.23.136 2.145.527 2.724 1.26.566.716.693 1.614.693 2.485 0 .572-.053 1.147-.254 1.655l.168.838.066.033A2.75 2.75 0 0 1 16 9.736V11c0 .24-.086.438-.156.567-.073.131-.16.253-.259.366-.18.21-.404.413-.605.58a10.19 10.19 0 0 1-.792.597l-.015.01-.006.004-.028.018a8.849 8.849 0 0 1-.456.281c-.307.177-.749.41-1.296.642C11.296 14.528 9.756 15 8 15c-1.756 0-3.296-.472-4.387-.935a12.28 12.28 0 0 1-1.296-.641 8.849 8.849 0 0 1-.456-.281l-.028-.02-.006-.003-.015-.01a10.593 10.593 0 0 1-.792-.596 5.264 5.264 0 0 1-.605-.58 2.133 2.133 0 0 1-.259-.367A1.189 1.189 0 0 1 0 11V9.736a2.75 2.75 0 0 1 1.52-2.46l.067-.033.167-.838C1.553 5.897 1.5 5.322 1.5 4.75c0-.87.127-1.77.693-2.485.579-.733 1.494-1.124 2.724-1.26 1.206-.134 2.262.034 2.944.765ZM3 7.824v4.261c.02.013.043.025.065.038.264.152.65.356 1.134.562.972.412 2.307.815 3.801.815 1.494 0 2.83-.403 3.8-.815.412-.174.813-.375 1.2-.6v-4.26l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.06-.328-2.71-.991A3.233 3.233 0 0 1 8 6.266c-.144.269-.321.52-.54.743C6.81 7.672 5.896 8 4.75 8c-.652 0-1.236-.082-1.726-.291L3 7.824Zm6.237-5.031c-.204.218-.359.678-.242 1.614.091.726.303 1.23.618 1.553.299.304.784.54 1.638.54.922 0 1.28-.199 1.442-.38.179-.2.308-.578.308-1.37 0-.765-.123-1.242-.37-1.555-.233-.296-.693-.586-1.713-.7-1.044-.116-1.488.091-1.681.298Zm-2.472 0c-.193-.207-.637-.414-1.681-.298-1.02.114-1.48.404-1.713.7-.247.313-.37.79-.37 1.555 0 .792.129 1.17.308 1.37.162.181.52.38 1.442.38.854 0 1.339-.236 1.638-.54.315-.323.527-.827.618-1.553.117-.936-.038-1.396-.242-1.614Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 gBKNLX react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 iJtJJh" href="/Frix-x/klippain/tree/main">klippain</a></li><li class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 iqTHmv">/</span><a sx="[object Object]" class="Link__StyledLink-sc-14289xe-0 hUWqlv" href="/Frix-x/klippain/tree/main/scripts">scripts</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 iqTHmv">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">system_info.py</h1></div></div><button type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 kGDoCG"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 bESQXL"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 ivYJSK"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 bFrOJy"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 gbKtit"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 dAXkSP"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 fOEJrA text-mono"><div title="executable file" class="Truncate__StyledTruncate-sc-23o1d2-0 eKEtoB"><span class="Text-sc-17v1xeu-0 gPDEWA">executable file</span></div><span class="Text-sc-17v1xeu-0 kfsdZq">·</span><div title="4.14 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">123 lines (97 loc) · 4.14 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-in-header"><button type="button" id=":R79jqlajal5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 cuVVHm"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6.25 9a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 6.25 9Zm4.25.75a.75.75 0 0 0-1.5 0v1.5a.75.75 0 0 0 1.5 0v-1.5Z"></path><path d="M7.86 1.77c.05.053.097.107.14.164.043-.057.09-.111.14-.164.681-.731 1.737-.9 2.943-.765 1.23.136 2.145.527 2.724 1.26.566.716.693 1.614.693 2.485 0 .572-.053 1.147-.254 1.655l.168.838.066.033A2.75 2.75 0 0 1 16 9.736V11c0 .24-.086.438-.156.567-.073.131-.16.253-.259.366-.18.21-.404.413-.605.58a10.19 10.19 0 0 1-.792.597l-.015.01-.006.004-.028.018a8.849 8.849 0 0 1-.456.281c-.307.177-.749.41-1.296.642C11.296 14.528 9.756 15 8 15c-1.756 0-3.296-.472-4.387-.935a12.28 12.28 0 0 1-1.296-.641 8.849 8.849 0 0 1-.456-.281l-.028-.02-.006-.003-.015-.01a10.593 10.593 0 0 1-.792-.596 5.264 5.264 0 0 1-.605-.58 2.133 2.133 0 0 1-.259-.367A1.189 1.189 0 0 1 0 11V9.736a2.75 2.75 0 0 1 1.52-2.46l.067-.033.167-.838C1.553 5.897 1.5 5.322 1.5 4.75c0-.87.127-1.77.693-2.485.579-.733 1.494-1.124 2.724-1.26 1.206-.134 2.262.034 2.944.765ZM3 7.824v4.261c.02.013.043.025.065.038.264.152.65.356 1.134.562.972.412 2.307.815 3.801.815 1.494 0 2.83-.403 3.8-.815.412-.174.813-.375 1.2-.6v-4.26l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.06-.328-2.71-.991A3.233 3.233 0 0 1 8 6.266c-.144.269-.321.52-.54.743C6.81 7.672 5.896 8 4.75 8c-.652 0-1.236-.082-1.726-.291L3 7.824Zm6.237-5.031c-.204.218-.359.678-.242 1.614.091.726.303 1.23.618 1.553.299.304.784.54 1.638.54.922 0 1.28-.199 1.442-.38.179-.2.308-.578.308-1.37 0-.765-.123-1.242-.37-1.555-.233-.296-.693-.586-1.713-.7-1.044-.116-1.488.091-1.681.298Zm-2.472 0c-.193-.207-.637-.414-1.681-.298-1.02.114-1.48.404-1.713.7-.247.313-.37.79-.37 1.555 0 .792.129 1.17.308 1.37.162.181.52.38 1.442.38.854 0 1.339-.236 1.638-.54.315-.323.527-.827.618-1.553.117-.936-.038-1.396-.242-1.614Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/Frix-x/klippain/raw/main/scripts/system_info.py" data-testid="raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hHvcfT"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kCdBku"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jcdBXR"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 bJBoUI js-github-dev-shortcut d-none" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 bJBoUI js-github-dev-new-tab-shortcut d-none" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="Fork this repository and edit the file" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bpoOwX" href="/Frix-x/klippain/edit/main/scripts/system_info.py"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":Rl7pjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kCdBku"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,E" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Close symbols panel" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="true" aria-expanded="true" aria-controls="symbols-pane" class="types__StyledButton-sc-ws60qy-0 bhUFcA" data-testid="symbols-button" id="symbols-button" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 jYfgHQ js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R1dpjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></div><div class="Box-sc-g0xbh4-0 etfROT"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 jWnGGx"><div class="Box-sc-g0xbh4-0 TCenl"><div id="highlighted-line-menu-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div class="Box-sc-g0xbh4-0 eRkHwF"><div class="Box-sc-g0xbh4-0 knCTAx react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers" style="pointer-events:auto"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right:16px">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right:16px">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right:16px">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right:16px">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right:16px">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right:16px">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right:16px">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right:16px">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right:16px">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right:16px">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right:16px">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right:16px">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right:16px">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right:16px">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right:16px">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right:16px">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right:16px">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right:16px">18</div><div data-line-number="19" class="react-line-number react-code-text" style="padding-right:16px">19</div><div data-line-number="20" class="react-line-number react-code-text" style="padding-right:16px">20</div><div data-line-number="21" class="react-line-number react-code-text" style="padding-right:16px">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right:16px">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right:16px">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right:16px">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right:16px">25<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="26" class="child-of-line-25  react-line-number react-code-text" style="padding-right:16px">26</div><div data-line-number="27" class="child-of-line-25  react-line-number react-code-text" style="padding-right:16px">27</div><div data-line-number="28" class="child-of-line-25  react-line-number react-code-text" style="padding-right:16px">28</div><div data-line-number="29" class="child-of-line-25  react-line-number react-code-text" style="padding-right:16px">29</div><div data-line-number="30" class="react-line-number react-code-text" style="padding-right:16px">30</div><div data-line-number="31" class="react-line-number react-code-text" style="padding-right:16px">31</div><div data-line-number="32" class="react-line-number react-code-text" style="padding-right:16px">32</div><div data-line-number="33" class="react-line-number react-code-text" style="padding-right:16px">33</div><div data-line-number="34" class="react-line-number react-code-text" style="padding-right:16px">34</div><div data-line-number="35" class="react-line-number react-code-text" style="padding-right:16px">35<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="36" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">36</div><div data-line-number="37" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">37</div><div data-line-number="38" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">38</div><div data-line-number="39" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">39</div><div data-line-number="40" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">40</div><div data-line-number="41" class="child-of-line-35  react-line-number react-code-text" style="padding-right:16px">41</div><div data-line-number="42" class="react-line-number react-code-text" style="padding-right:16px">42</div><div data-line-number="43" class="react-line-number react-code-text" style="padding-right:16px">43</div><div data-line-number="44" class="react-line-number react-code-text" style="padding-right:16px">44<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="45" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">45</div><div data-line-number="46" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">46</div><div data-line-number="47" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">47</div><div data-line-number="48" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">48</div><div data-line-number="49" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">49</div><div data-line-number="50" class="child-of-line-44  react-line-number react-code-text" style="padding-right:16px">50</div><div data-line-number="51" class="react-line-number react-code-text" style="padding-right:16px">51</div><div data-line-number="52" class="react-line-number react-code-text" style="padding-right:16px">52</div><div data-line-number="53" class="react-line-number react-code-text" style="padding-right:16px">53<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="54" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">54</div><div data-line-number="55" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">55</div><div data-line-number="56" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">56</div><div data-line-number="57" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">57</div><div data-line-number="58" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">58</div><div data-line-number="59" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">59</div><div data-line-number="60" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">60</div><div data-line-number="61" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">61</div><div data-line-number="62" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">62</div><div data-line-number="63" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">63</div><div data-line-number="64" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">64</div><div data-line-number="65" class="child-of-line-53  react-line-number react-code-text" style="padding-right:16px">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right:16px">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right:16px">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right:16px">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right:16px">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right:16px">70</div><div data-line-number="71" class="react-line-number react-code-text" style="padding-right:16px">71</div><div data-line-number="72" class="react-line-number react-code-text" style="padding-right:16px">72<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="73" class="child-of-line-72  react-line-number react-code-text" style="padding-right:16px">73</div><div data-line-number="74" class="child-of-line-72  react-line-number react-code-text" style="padding-right:16px">74</div><div data-line-number="75" class="child-of-line-72  react-line-number react-code-text" style="padding-right:16px">75</div><div data-line-number="76" class="child-of-line-72  react-line-number react-code-text" style="padding-right:16px">76</div><div data-line-number="77" class="child-of-line-72  react-line-number react-code-text" style="padding-right:16px">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right:16px">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right:16px">79</div><div data-line-number="80" class="react-line-number react-code-text" style="padding-right:16px">80</div><div data-line-number="81" class="react-line-number react-code-text" style="padding-right:16px">81<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="82" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">82</div><div data-line-number="83" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">83</div><div data-line-number="84" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">84</div><div data-line-number="85" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">85</div><div data-line-number="86" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">86</div><div data-line-number="87" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">87</div><div data-line-number="88" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">88</div><div data-line-number="89" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">89</div><div data-line-number="90" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">90</div><div data-line-number="91" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">91</div><div data-line-number="92" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">92</div><div data-line-number="93" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">93</div><div data-line-number="94" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">94</div><div data-line-number="95" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">95</div><div data-line-number="96" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">96</div><div data-line-number="97" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">97</div><div data-line-number="98" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">98</div><div data-line-number="99" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">99</div><div data-line-number="100" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">100</div><div data-line-number="101" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">101</div><div data-line-number="102" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">102</div><div data-line-number="103" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">103</div><div data-line-number="104" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">104</div><div data-line-number="105" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">105</div><div data-line-number="106" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">106</div><div data-line-number="107" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">107</div><div data-line-number="108" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">108</div><div data-line-number="109" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">109</div><div data-line-number="110" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">110</div><div data-line-number="111" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">111</div><div data-line-number="112" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">112</div><div data-line-number="113" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">113</div><div data-line-number="114" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">114</div><div data-line-number="115" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">115</div><div data-line-number="116" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">116</div><div data-line-number="117" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">117</div><div data-line-number="118" class="child-of-line-81  react-line-number react-code-text" style="padding-right:16px">118</div><div data-line-number="119" class="react-line-number react-code-text" style="padding-right:16px">119</div><div data-line-number="120" class="react-line-number react-code-text" style="padding-right:16px">120</div><div data-line-number="121" class="react-line-number react-code-text" style="padding-right:16px">121</div><div data-line-number="122" class="react-line-number react-code-text" style="padding-right:16px">122</div><div data-line-number="123" class="react-line-number react-code-text" style="padding-right:16px">123</div></div><div class="react-code-lines"><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" style="position:relative"><span class="pl-c">#!/usr/bin/env python3</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" style="position:relative"><span class="pl-c">######################################</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" style="position:relative"><span class="pl-c">###### BASIC SYSTEM INFO SCRIPT ######</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" style="position:relative"><span class="pl-c">######################################</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" style="position:relative"><span class="pl-c"># Written by Frix_x#0161 #</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" style="position:relative"><span class="pl-c"># @version: 1.0</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" style="position:relative"><span class="pl-c"># CHANGELOG:</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" style="position:relative"><span class="pl-c">#   v1.0: first version of the script to get some system info printed in the klippy.log</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" style="position:relative"><span class="pl-c"># Be sure to make this script executable using SSH: type &#039;chmod +x ./system_info.py&#039; when in the folder !</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" style="position:relative"><span class="pl-c">#####################################################################</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" style="position:relative"><span class="pl-c">################ !!! DO NOT EDIT BELOW THIS LINE !!! ################</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" style="position:relative"><span class="pl-c">#####################################################################</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" style="position:relative"><span class="pl-k">import</span> <span class="pl-s1">subprocess</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" style="position:relative"><span class="pl-k">import</span> <span class="pl-s1">os</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" style="position:relative"><span class="pl-k">import</span> <span class="pl-s1">platform</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" style="position:relative"><span class="pl-k">from</span> <span class="pl-s1">datetime</span> <span class="pl-k">import</span> <span class="pl-s1">datetime</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" style="position:relative"><span class="pl-k">import</span> <span class="pl-s1">concurrent</span>.<span class="pl-s1">futures</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">get_date_time</span>():</div></div></div><div class="child-of-line-25  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" style="position:relative">    <span class="pl-c"># Special note for power-user running Klipper inside a docker container: usually the timezone</span></div></div></div><div class="child-of-line-25  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" style="position:relative">    <span class="pl-c"># is not set and this result in a print of the UTC time (instead of local). Consider running</span></div></div></div><div class="child-of-line-25  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" style="position:relative">    <span class="pl-c"># the container like: &quot;docker run -e TZ=America/New_York klipper_image&quot;</span></div></div></div><div class="child-of-line-25  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" style="position:relative">    <span class="pl-c"># in order to get a proper timezone set and get the correct time read by this script</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s1">datetime</span>.<span class="pl-en">now</span>().<span class="pl-en">strftime</span>(<span class="pl-s">&quot;%m/%d/%Y, %H:%M:%S&quot;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">check_docker</span>():</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">exists</span>(<span class="pl-s">&#039;/.dockerenv&#039;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">check_wsl</span>():</div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" style="position:relative">    <span class="pl-k">try</span>:</div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" style="position:relative">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">&#039;/proc/version&#039;</span>, <span class="pl-s">&#039;r&#039;</span>) <span class="pl-k">as</span> <span class="pl-s1">f</span>:</div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" style="position:relative">            <span class="pl-k">if</span> <span class="pl-s">&#039;microsoft&#039;</span> <span class="pl-c1">in</span> <span class="pl-s1">f</span>.<span class="pl-en">read</span>().<span class="pl-en">lower</span>():</div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" style="position:relative">                <span class="pl-k">return</span> <span class="pl-c1">True</span></div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" style="position:relative">    <span class="pl-k">except</span> <span class="pl-v">Exception</span>:</div></div></div><div class="child-of-line-35  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" style="position:relative">        <span class="pl-k">pass</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" style="position:relative">    <span class="pl-k">return</span> <span class="pl-c1">False</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">get_pi_model</span>():</div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" style="position:relative">    <span class="pl-k">try</span>:</div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" style="position:relative">        <span class="pl-s1">model_info</span> <span class="pl-c1">=</span> <span class="pl-s1">subprocess</span>.<span class="pl-en">check_output</span>([<span class="pl-s">&#039;cat&#039;</span>, <span class="pl-s">&#039;/sys/firmware/devicetree/base/model&#039;</span>], <span class="pl-s1">universal_newlines</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" style="position:relative">        <span class="pl-k">if</span> <span class="pl-s">&#039;raspberry pi&#039;</span> <span class="pl-c1">in</span> <span class="pl-s1">model_info</span>.<span class="pl-en">lower</span>(): <span class="pl-k">return</span> <span class="pl-s1">model_info</span></div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" style="position:relative">    <span class="pl-k">except</span> <span class="pl-s1">subprocess</span>.<span class="pl-v">CalledProcessError</span>:</div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" style="position:relative">        <span class="pl-k">return</span> <span class="pl-c1">None</span></div></div></div><div class="child-of-line-44  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" style="position:relative">    <span class="pl-k">else</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" style="position:relative">        <span class="pl-k">return</span> <span class="pl-c1">None</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">get_unknown_board_info</span>():</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" style="position:relative">    <span class="pl-k">try</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" style="position:relative">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">&#039;/proc/cpuinfo&#039;</span>, <span class="pl-s">&#039;r&#039;</span>) <span class="pl-k">as</span> <span class="pl-s1">f</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" style="position:relative">            <span class="pl-k">for</span> <span class="pl-s1">line</span> <span class="pl-c1">in</span> <span class="pl-s1">f</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" style="position:relative">                <span class="pl-k">if</span> <span class="pl-s1">line</span>.<span class="pl-en">startswith</span>(<span class="pl-s">&#039;Hardware&#039;</span>) <span class="pl-c1">or</span> <span class="pl-s1">line</span>.<span class="pl-en">startswith</span>(<span class="pl-s">&#039;Model&#039;</span>):</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" style="position:relative">                    <span class="pl-k">return</span> <span class="pl-s1">line</span>.<span class="pl-en">split</span>(<span class="pl-s">&#039;:&#039;</span>)[<span class="pl-c1">1</span>].<span class="pl-en">strip</span>()</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" style="position:relative">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">&#039;/etc/os-release&#039;</span>, <span class="pl-s">&#039;r&#039;</span>) <span class="pl-k">as</span> <span class="pl-s1">f</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" style="position:relative">            <span class="pl-k">for</span> <span class="pl-s1">line</span> <span class="pl-c1">in</span> <span class="pl-s1">f</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" style="position:relative">                <span class="pl-k">if</span> <span class="pl-s1">line</span>.<span class="pl-en">startswith</span>(<span class="pl-s">&#039;PRETTY_NAME&#039;</span>) <span class="pl-c1">or</span> <span class="pl-s1">line</span>.<span class="pl-en">startswith</span>(<span class="pl-s">&#039;NAME&#039;</span>):</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" style="position:relative">                    <span class="pl-k">return</span> <span class="pl-s1">line</span>.<span class="pl-en">split</span>(<span class="pl-s">&#039;=&#039;</span>)[<span class="pl-c1">1</span>].<span class="pl-en">strip</span>().<span class="pl-en">strip</span>(<span class="pl-s">&#039;&quot;&#039;</span>)</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" style="position:relative">    <span class="pl-k">except</span> <span class="pl-v">Exception</span>:</div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" style="position:relative">        <span class="pl-k">pass</span></div></div></div><div class="child-of-line-53  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s">&quot;no additional info...&quot;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">get_os_kernel_info</span>():</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" style="position:relative">    <span class="pl-s1">uname</span> <span class="pl-c1">=</span> <span class="pl-s1">os</span>.<span class="pl-en">uname</span>()</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" style="position:relative">    <span class="pl-k">return</span> <span class="pl-s1">uname</span>.<span class="pl-s1">sysname</span>, <span class="pl-s1">uname</span>.<span class="pl-s1">release</span>, <span class="pl-s1">uname</span>.<span class="pl-s1">machine</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">get_ram_info</span>():</div></div></div><div class="child-of-line-72  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" style="position:relative">    <span class="pl-k">try</span>:</div></div></div><div class="child-of-line-72  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" style="position:relative">        <span class="pl-s1">total_ram</span> <span class="pl-c1">=</span> <span class="pl-s1">subprocess</span>.<span class="pl-en">check_output</span>([<span class="pl-s">&#039;free&#039;</span>, <span class="pl-s">&#039;-m&#039;</span>], <span class="pl-s1">universal_newlines</span><span class="pl-c1">=</span><span class="pl-c1">True</span>).<span class="pl-en">split</span>(<span class="pl-s">&#039;<span class="pl-cce">\n</span>&#039;</span>)[<span class="pl-c1">1</span>].<span class="pl-en">split</span>()[<span class="pl-c1">1</span>]</div></div></div><div class="child-of-line-72  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" style="position:relative">        <span class="pl-s1">available_ram</span> <span class="pl-c1">=</span> <span class="pl-s1">subprocess</span>.<span class="pl-en">check_output</span>([<span class="pl-s">&#039;free&#039;</span>, <span class="pl-s">&#039;-m&#039;</span>], <span class="pl-s1">universal_newlines</span><span class="pl-c1">=</span><span class="pl-c1">True</span>).<span class="pl-en">split</span>(<span class="pl-s">&#039;<span class="pl-cce">\n</span>&#039;</span>)[<span class="pl-c1">1</span>].<span class="pl-en">split</span>()[<span class="pl-c1">6</span>]</div></div></div><div class="child-of-line-72  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" style="position:relative">        <span class="pl-k">return</span> <span class="pl-s1">total_ram</span>, <span class="pl-s1">available_ram</span></div></div></div><div class="child-of-line-72  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" style="position:relative">    <span class="pl-k">except</span> <span class="pl-s1">subprocess</span>.<span class="pl-v">CalledProcessError</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" style="position:relative">        <span class="pl-k">return</span> <span class="pl-c1">None</span>, <span class="pl-c1">None</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" style="position:relative"><span class="pl-k">def</span> <span class="pl-en">print_system_info</span>():</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" style="position:relative">    <span class="pl-k">with</span> <span class="pl-s1">concurrent</span>.<span class="pl-s1">futures</span>.<span class="pl-v">ThreadPoolExecutor</span>() <span class="pl-k">as</span> <span class="pl-s1">executor</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" style="position:relative">        <span class="pl-s1">future_date_time</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">get_date_time</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" style="position:relative">        <span class="pl-s1">future_docker</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">check_docker</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" style="position:relative">        <span class="pl-s1">future_pi_model</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">get_pi_model</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" style="position:relative">        <span class="pl-s1">future_wsl</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">check_wsl</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" style="position:relative">        <span class="pl-s1">future_os_kernel</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">get_os_kernel_info</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" style="position:relative">        <span class="pl-s1">future_ram_info</span> <span class="pl-c1">=</span> <span class="pl-s1">executor</span>.<span class="pl-en">submit</span>(<span class="pl-s1">get_ram_info</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" style="position:relative">    <span class="pl-s1">date_time</span> <span class="pl-c1">=</span> <span class="pl-s1">future_date_time</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" style="position:relative">    <span class="pl-en">print</span>(<span class="pl-s">f&quot;Klippain started (<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">date_time</span><span class="pl-kos">}</span></span>)&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" style="position:relative">    <span class="pl-s1">sysname</span>, <span class="pl-s1">release</span>, <span class="pl-s1">machine</span> <span class="pl-c1">=</span> <span class="pl-s1">future_os_kernel</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" style="position:relative">    <span class="pl-en">print</span>(<span class="pl-s">f&quot;Operating System: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">sysname</span><span class="pl-kos">}</span></span> - <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">release</span><span class="pl-kos">}</span></span>&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" style="position:relative">    <span class="pl-s1">is_docker</span> <span class="pl-c1">=</span> <span class="pl-s1">future_docker</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" style="position:relative">    <span class="pl-s1">is_wsl</span> <span class="pl-c1">=</span> <span class="pl-s1">future_wsl</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" style="position:relative">    <span class="pl-s1">pi_model</span> <span class="pl-c1">=</span> <span class="pl-s1">future_pi_model</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">is_docker</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;Machine: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">machine</span><span class="pl-kos">}</span></span> - in a docker container&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" style="position:relative">    <span class="pl-k">elif</span> <span class="pl-s1">is_wsl</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;Machine: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">machine</span><span class="pl-kos">}</span></span> - in Windows Subsystem for Linux&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" style="position:relative">    <span class="pl-k">elif</span> <span class="pl-s1">pi_model</span> <span class="pl-c1">is</span> <span class="pl-c1">not</span> <span class="pl-c1">None</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;Machine: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">machine</span><span class="pl-kos">}</span></span> - in a <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">pi_model</span><span class="pl-kos">}</span></span>&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" style="position:relative">    <span class="pl-k">else</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" style="position:relative">        <span class="pl-c"># This is the case where it is running on a unknown machine type</span></div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" style="position:relative">        <span class="pl-c"># so we use the specific function to try to gather more info...</span></div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;Machine: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">machine</span><span class="pl-kos">}</span></span>&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;System information: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-en">get_unknown_board_info</span>()<span class="pl-kos">}</span></span>&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" style="position:relative">
</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" style="position:relative">    <span class="pl-s1">total_ram</span>, <span class="pl-s1">available_ram</span> <span class="pl-c1">=</span> <span class="pl-s1">future_ram_info</span>.<span class="pl-en">result</span>()</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" style="position:relative">    <span class="pl-k">if</span> <span class="pl-s1">total_ram</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span> <span class="pl-c1">or</span> <span class="pl-s1">available_ram</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span>:</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">&quot;RAM information not found...&quot;</span>)</div></div></div><div class="child-of-line-81  react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" style="position:relative">    <span class="pl-k">else</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC119" class="react-file-line html-div" data-testid="code-cell" data-line-number="119" style="position:relative">        <span class="pl-en">print</span>(<span class="pl-s">f&quot;Used RAM: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">available_ram</span><span class="pl-kos">}</span></span>/<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">total_ram</span><span class="pl-kos">}</span></span> MB&quot;</span>)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC120" class="react-file-line html-div" data-testid="code-cell" data-line-number="120" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC121" class="react-file-line html-div" data-testid="code-cell" data-line-number="121" style="position:relative">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC122" class="react-file-line html-div" data-testid="code-cell" data-line-number="122" style="position:relative"><span class="pl-k">if</span> <span class="pl-s1">__name__</span> <span class="pl-c1">==</span> <span class="pl-s">&quot;__main__&quot;</span>:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height:auto"><div><div id="LC123" class="react-file-line html-div" data-testid="code-cell" data-line-number="123" style="position:relative">    <span class="pl-en">print_system_info</span>()</div></div></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div><button hidden="" data-testid="hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></section></div></div><div class="Box-sc-g0xbh4-0 ktQnIo"></div><div class="Box-sc-g0xbh4-0 bgyiQy panel-content-narrow-styles inner-panel-content-not-narrow"><div id="symbols-pane" class="Box-sc-g0xbh4-0"><div aria-labelledby="symbols-pane-header" class="Box-sc-g0xbh4-0 bJNAmt"><div class="Box-sc-g0xbh4-0 ipXucK"><h2 id="symbols-pane-header" tabindex="-1" class="Box-sc-g0xbh4-0 wMEyi">Symbols</h2><button data-component="IconButton" type="button" aria-label="Close symbols" data-hotkey="Escape" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iGBjJv"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button></div><div class="Box-sc-g0xbh4-0 OThit">Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code.</div><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 fBrOQk jnWkuY TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M.75 3h14.5a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1 0-1.5ZM3 7.75A.75.75 0 0 1 3.75 7h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 7.75Zm3 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg></span><input type="text" placeholder="Filter symbols" name="Filter symbols" aria-label="Filter symbols" aria-controls="filter-results" aria-expanded="true" aria-autocomplete="list" role="combobox" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""/><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 ckwgci"><kbd>r</kbd></div></span></span><div class="Box-sc-g0xbh4-0 jGYebd"><div class="Box-sc-g0xbh4-0 kgNotW"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Code Navigation" data-omit-spacer="true" class="TreeView__UlBox-sc-4ex6b6-0 hLwWNO"><li class="PRIVATE_TreeView-item" tabindex="0" id="0get_date_time" role="treeitem" aria-labelledby=":R6hlqlajal5:" aria-describedby=":R6hlqlajal5H1: :R6hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="get_date_time" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">get_date_time</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="1check_docker" role="treeitem" aria-labelledby=":Rahlqlajal5:" aria-describedby=":Rahlqlajal5H1: :Rahlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rahlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="check_docker" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">check_docker</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="2check_wsl" role="treeitem" aria-labelledby=":Rehlqlajal5:" aria-describedby=":Rehlqlajal5H1: :Rehlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rehlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="check_wsl" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">check_wsl</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="3get_pi_model" role="treeitem" aria-labelledby=":Rihlqlajal5:" aria-describedby=":Rihlqlajal5H1: :Rihlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rihlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="get_pi_model" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">get_pi_model</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="4get_unknown_board_info" role="treeitem" aria-labelledby=":Rmhlqlajal5:" aria-describedby=":Rmhlqlajal5H1: :Rmhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rmhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="get_unknown_board_info" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">get_unknown_board_info</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="5get_os_kernel_info" role="treeitem" aria-labelledby=":Rqhlqlajal5:" aria-describedby=":Rqhlqlajal5H1: :Rqhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rqhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="get_os_kernel_info" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">get_os_kernel_info</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="6get_ram_info" role="treeitem" aria-labelledby=":Ruhlqlajal5:" aria-describedby=":Ruhlqlajal5H1: :Ruhlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Ruhlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="get_ram_info" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">get_ram_info</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="7print_system_info" role="treeitem" aria-labelledby=":R12hlqlajal5:" aria-describedby=":R12hlqlajal5H1: :R12hlqlajal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R12hlqlajal5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 kpISzB"></div><div class="Box-sc-g0xbh4-0 aiXQv">func</div></div>  <div title="print_system_info" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">print_system_info</span></div></div></span></div></div></li></ul></div></div></div></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></main></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></div> <!-- --> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive" role="contentinfo">
  <h2 class='sr-only'>Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>        <span>
        &copy; 2023 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label='Footer' class="col-12 col-lg-8">
      <h3 class='sr-only' id='sr-footer-heading'>Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby='sr-footer-heading'>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>


    <style>
      .user-mention[href$="/Westy69"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" ></div>
  </body>
</html>
