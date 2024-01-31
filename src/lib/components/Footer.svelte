<script>
  const sponsors = [
    {
      name: "SACDA",
      link: "http://sacda.ca",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/sacda.svg",
    },
    {
      name: "South Asian Studies Institute",
      link: "http://www.ufv.ca/sasi",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/sasi.svg",
    },
    {
      name: "University of the Fraser Valley",
      link: "http://www.ufv.ca/",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/ufv.svg",
    },
    {
      name: "South Asian Canadian Legacy Project",
      link: "https://saclp.southasiancanadianheritage.ca/",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/bc.svg",
    },
    {
      name: "Canada",
      link: "https://www.canada.ca/en.html",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/canada_logo.svg",
    },
    {
      name: "UBC Irving K. Barber Learning Centre",
      link: "https://ikblc.ubc.ca/",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/BCHDP_logo_white.png",
    },
  ];

  const socials = [
    {
      name: "Facebook",
      link: "https://www.facebook.com/profile.php?id=100092345694324",
      element: "<i class='fa fa-facebook-square'></i>",
    },
    {
      name: "Instagram",
      link: "https://www.instagram.com/sacda.sasi/",
      element: "<i class='fa fa-instagram'></i>",
    },
    {
      name: "Twitter",
      link: "https://twitter.com/ufvsasi",
      element: "<i class='fa fa-twitter'></i>",
    },
    {
      name: "Youtube",
      link: "https://www.youtube.com/channel/UCN5tvG-Q8ly9z0YOyWsoaNA",
      element: "<i class='fa fa-youtube'></i>",
    },
    {
      name: "Flicker",
      link: "https://www.flickr.com/photos/ufvcics/albums",
      element: "<i class='fa fa-flickr'></i>",
    },
  ];
</script>

<footer class="bg-[#414042] py-24 px-6 flex justify-between items-end relative">
  <div class="flex flex-row gap-5 items-center pb-3">
    {#each sponsors as sponsor}
      <div class="w-auto">
        <a href={sponsor.link} target="_blank" rel="noopener noreferrer">
          <img src={sponsor.image} alt={sponsor.name} class="h-10" />
        </a>
      </div>
    {/each}
  </div>

  <div class="flex flex-col gap-4 w-fit">
    <p
      class="uppercase self-end border-b border-b-[#ffce34] font-bold text-white text-lg w-fit pb-1"
    >
      GET IN TOUCH
    </p>

    <div class="flex flex-row gap-3">
      {#each socials as social}
        <a
          href={social.link}
          target="_blank"
          rel="noopener noreferrer"
          class="text-white text-lg rounded-full border border-[#ffce34] w-12 h-12 flex items-center justify-center"
        >
          {@html social.element}
        </a>
      {/each}
    </div>
  </div>

  <div class="absolute bottom-6 text-white text-sm">
    Statement of Use and Takedown Policy | Media | © 2024 South Asian Canadian
    Digital Archive
  </div>
</footer>
