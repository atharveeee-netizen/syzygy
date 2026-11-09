// SYZYGY Auth Middleware Boilerplate (Clerk)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

// Note: Ensure NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY is set in your .env.local

const isPublicRoute = createRouteMatcher(['/sign-in(.*)', '/sign-up(.*)', '/', '/api/webhook(.*)']);

export default clerkMiddleware(async (auth, request) => {
  if (!isPublicRoute(request)) {
    await auth.protect();
  }
});

export const config = {
  matcher: [
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/(api|trpc)(.*)',
  ],
};
