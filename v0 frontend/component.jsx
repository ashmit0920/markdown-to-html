/**
 * v0 by Vercel.
 * @see https://v0.dev/t/JdlSTfK7Mqn
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
 import Link from "next/link"
 import { Button } from "@/components/ui/button"
 import { Input } from "@/components/ui/input"
 
 export default function Component() {
   return (
     <div className="dark bg-[#1a1b1e] text-white min-h-screen flex flex-col">
       <header className="py-6 px-4 md:px-8 flex items-center justify-between border-b border-[#2c2d30]">
         <Link href="#" className="flex items-center gap-2" prefetch={false}>
           <TerminalIcon className="h-6 w-6 text-primary" />
           <span className="text-lg font-medium">Techscape</span>
         </Link>
         <nav className="hidden md:flex items-center gap-4">
           <Link href="#" className="text-sm font-medium hover:text-primary transition" prefetch={false}>
             Features
           </Link>
           <Link href="#" className="text-sm font-medium hover:text-primary transition" prefetch={false}>
             Pricing
           </Link>
           <Link href="#" className="text-sm font-medium hover:text-primary transition" prefetch={false}>
             Contact
           </Link>
         </nav>
         <Button className="hidden md:inline-flex">Get Started</Button>
       </header>
       <main className="flex-1 flex flex-col items-center justify-center px-4 md:px-8 py-12 md:py-20">
         <div className="max-w-3xl text-center space-y-4">
           <h1 className="text-4xl md:text-6xl font-bold tracking-tight">Elevate Your Digital Presence</h1>
           <p className="text-muted-foreground text-lg md:text-xl">
             Unlock the power of our cutting-edge technology to transform your online experience.
           </p>
           <div className="flex flex-col sm:flex-row items-center gap-4">
             <Input
               type="file"
               id="file-upload"
               className="file:bg-primary file:text-primary-foreground file:border-none file:rounded-md file:px-4 file:py-2 file:mr-4 file:cursor-pointer"
             />
             <Button>Upload File</Button>
           </div>
         </div>
       </main>
       <footer className="py-6 px-4 md:px-8 border-t border-[#2c2d30] text-muted-foreground text-sm">
         <div className="container mx-auto flex items-center justify-between">
           <p>&copy; 2024 Techscape. All rights reserved.</p>
           <nav className="flex items-center gap-4">
             <Link href="#" className="hover:text-primary transition" prefetch={false}>
               Privacy
             </Link>
             <Link href="#" className="hover:text-primary transition" prefetch={false}>
               Terms
             </Link>
             <Link href="#" className="hover:text-primary transition" prefetch={false}>
               Contact
             </Link>
           </nav>
         </div>
       </footer>
     </div>
   )
 }
 
 function TerminalIcon(props) {
   return (
     <svg
       {...props}
       xmlns="http://www.w3.org/2000/svg"
       width="24"
       height="24"
       viewBox="0 0 24 24"
       fill="none"
       stroke="currentColor"
       strokeWidth="2"
       strokeLinecap="round"
       strokeLinejoin="round"
     >
       <polyline points="4 17 10 11 4 5" />
       <line x1="12" x2="20" y1="19" y2="19" />
     </svg>
   )
 }
 
 
 function XIcon(props) {
   return (
     <svg
       {...props}
       xmlns="http://www.w3.org/2000/svg"
       width="24"
       height="24"
       viewBox="0 0 24 24"
       fill="none"
       stroke="currentColor"
       strokeWidth="2"
       strokeLinecap="round"
       strokeLinejoin="round"
     >
       <path d="M18 6 6 18" />
       <path d="m6 6 12 12" />
     </svg>
   )
 }